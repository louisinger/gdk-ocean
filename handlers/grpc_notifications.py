import asyncio
from typing import Dict, List
from domain.notification import BaseNotification, NotificationType
from ocean.v1alpha import notification_pb2, notification_pb2_grpc

class _Subscriber():
    def __init__(self, subscribe_to: List[NotificationType]) -> None:
        # it lets to limit the number of notifications in the queue for each subscriber
        # so the subscriber can't block the server
        MAX_QUEUE_SIZE = 100
        
        self.type: str = None
        self.queue = asyncio.Queue(MAX_QUEUE_SIZE)
        self._types_to_broadcast = subscribe_to
        
    def put(self, notification: BaseNotification) -> None:
        if notification.type in self._types_to_broadcast:
            self.queue.put_nowait(notification)
        
    async def get(self) -> BaseNotification:
        next_notification = await self.queue.get()
        return next_notification

class GrpcNotificationsServicer(notification_pb2_grpc.NotificationServiceServicer):
    def __init__(self) -> None:
        self.task: asyncio.Task = None
        self._notifications_queue = asyncio.Queue()
        self._subscribers: Dict[int, _Subscriber] = {}
        self.next_id = 0
    
    @classmethod
    async def create(cls, q: asyncio.Queue):
        self = cls()
        self._notifications_queue = q
        self.task = asyncio.create_task(self._consumer())
        return self
        
    async def _consumer(self):
        while True:
            notification = await self._notifications_queue.get()
            for subscriber in self._subscribers.values():
                subscriber.put(notification)
            self._notifications_queue.task_done()
        
    async def TransactionNotifications(self, request: notification_pb2.TransactionNotificationsRequest, context):
        self._svc.add_txs_check_account(request.account_name)
        notifs_q = asyncio.Queue()
        self._subscribers.add(notifs_q)
        while True:
            notification = await notifs_q.get()
            yield notification