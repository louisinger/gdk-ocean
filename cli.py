from email.policy import default
import click
import grpc
from ocean.v1alpha import wallet_pb2_grpc, wallet_pb2

def _get_wallet_stub_from_context(ctx: click.Context) -> wallet_pb2_grpc.WalletServiceStub:
    return ctx.obj['wallet']

@click.group()
@click.option('--verbose', is_flag=True, default=False)
@click.option('--host', default='localhost')
@click.option('--port', default=50051)
@click.pass_context
def cli(ctx: click.Context, verbose: bool, host: str, port: int):
    """
    A command line interface for Gdk-ocean.
    """
    channel = grpc.insecure_channel(f'{host}:{port}')
    stub = wallet_pb2_grpc.WalletServiceStub(channel)
    
    ctx.ensure_object(dict)
    ctx.obj['verbose'] = verbose
    ctx.obj['wallet'] = stub
    
    global verbose_flag
    verbose_flag = verbose
    
@cli.command()
@click.pass_context
def genseed(ctx: click.Context):
    """
    Generate a random seed.
    """
    wallet_stub = _get_wallet_stub_from_context(ctx)
    seed = wallet_stub.GenSeed(wallet_pb2.GenSeedRequest())
    print(seed)

@cli.command()
@click.option('--mnemonic', '-m', default=None)
@click.option('--password', '-p', default=None)
@click.pass_context
def create(ctx: click.Context, mnemonic: str, password: str):
    request = wallet_pb2.CreateWalletRequest()
    request.mnemonic = mnemonic
    request.password = password.encode('utf-8')
    
    wallet_stub = _get_wallet_stub_from_context(ctx)
    response = wallet_stub.CreateWallet(request)
    print(response)


@cli.command()
@click.option('--password', '-p', default=None)
@click.pass_context
def unlock(ctx: click.Context, password: str):
    request = wallet_pb2.UnlockRequest()
    request.password = password.encode('utf-8')
    wallet_stub = _get_wallet_stub_from_context(ctx)
    response = wallet_stub.Unlock(request)
    print(response)

if __name__ == '__main__':
    cli(obj={})