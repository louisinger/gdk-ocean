# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ocean/v1/wallet.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ocean.v1 import types_pb2 as ocean_dot_v1_dot_types__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15ocean/v1/wallet.proto\x12\x08ocean.v1\x1a\x14ocean/v1/types.proto\"\x10\n\x0eGenSeedRequest\"-\n\x0fGenSeedResponse\x12\x1a\n\x08mnemonic\x18\x01 \x01(\tR\x08mnemonic\"M\n\x13\x43reateWalletRequest\x12\x1a\n\x08mnemonic\x18\x01 \x01(\tR\x08mnemonic\x12\x1a\n\x08password\x18\x03 \x01(\tR\x08password\"\x16\n\x14\x43reateWalletResponse\"+\n\rUnlockRequest\x12\x1a\n\x08password\x18\x01 \x01(\tR\x08password\"\x10\n\x0eUnlockResponse\")\n\x0bLockRequest\x12\x1a\n\x08password\x18\x01 \x01(\tR\x08password\"\x0e\n\x0cLockResponse\"e\n\x15\x43hangePasswordRequest\x12)\n\x10\x63urrent_password\x18\x01 \x01(\tR\x0f\x63urrentPassword\x12!\n\x0cnew_password\x18\x02 \x01(\tR\x0bnewPassword\"\x18\n\x16\x43hangePasswordResponse\"~\n\x14RestoreWalletRequest\x12\x1a\n\x08mnemonic\x18\x01 \x01(\tR\x08mnemonic\x12\x1a\n\x08password\x18\x02 \x01(\tR\x08password\x12.\n\x13\x62irthday_block_hash\x18\x03 \x01(\tR\x11\x62irthdayBlockHash\"\x17\n\x15RestoreWalletResponse\"\x0f\n\rStatusRequest\"f\n\x0eStatusResponse\x12 \n\x0binitialized\x18\x01 \x01(\x08R\x0binitialized\x12\x16\n\x06synced\x18\x02 \x01(\x08R\x06synced\x12\x1a\n\x08unlocked\x18\x03 \x01(\x08R\x08unlocked\"\x10\n\x0eGetInfoRequest\"\xec\x03\n\x0fGetInfoResponse\x12;\n\x07network\x18\x01 \x01(\x0e\x32!.ocean.v1.GetInfoResponse.NetworkR\x07network\x12!\n\x0cnative_asset\x18\x02 \x01(\tR\x0bnativeAsset\x12\x1b\n\troot_path\x18\x03 \x01(\tR\x08rootPath\x12.\n\x13master_blinding_key\x18\x04 \x01(\tR\x11masterBlindingKey\x12.\n\x13\x62irthday_block_hash\x18\x05 \x01(\tR\x11\x62irthdayBlockHash\x12\x32\n\x15\x62irthday_block_height\x18\x06 \x01(\rR\x13\x62irthdayBlockHeight\x12\x31\n\x08\x61\x63\x63ounts\x18\x07 \x03(\x0b\x32\x15.ocean.v1.AccountInfoR\x08\x61\x63\x63ounts\x12\x32\n\nbuild_info\x18\x08 \x01(\x0b\x32\x13.ocean.v1.BuildInfoR\tbuildInfo\"a\n\x07Network\x12\x17\n\x13NETWORK_UNSPECIFIED\x10\x00\x12\x13\n\x0fNETWORK_MAINNET\x10\x01\x12\x13\n\x0fNETWORK_TESTNET\x10\x02\x12\x13\n\x0fNETWORK_REGTEST\x10\x03\x32\xb6\x04\n\rWalletService\x12>\n\x07GenSeed\x12\x18.ocean.v1.GenSeedRequest\x1a\x19.ocean.v1.GenSeedResponse\x12M\n\x0c\x43reateWallet\x12\x1d.ocean.v1.CreateWalletRequest\x1a\x1e.ocean.v1.CreateWalletResponse\x12;\n\x06Unlock\x12\x17.ocean.v1.UnlockRequest\x1a\x18.ocean.v1.UnlockResponse\x12\x35\n\x04Lock\x12\x15.ocean.v1.LockRequest\x1a\x16.ocean.v1.LockResponse\x12S\n\x0e\x43hangePassword\x12\x1f.ocean.v1.ChangePasswordRequest\x1a .ocean.v1.ChangePasswordResponse\x12P\n\rRestoreWallet\x12\x1e.ocean.v1.RestoreWalletRequest\x1a\x1f.ocean.v1.RestoreWalletResponse\x12;\n\x06Status\x12\x17.ocean.v1.StatusRequest\x1a\x18.ocean.v1.StatusResponse\x12>\n\x07GetInfo\x12\x18.ocean.v1.GetInfoRequest\x1a\x19.ocean.v1.GetInfoResponseb\x06proto3')



_GENSEEDREQUEST = DESCRIPTOR.message_types_by_name['GenSeedRequest']
_GENSEEDRESPONSE = DESCRIPTOR.message_types_by_name['GenSeedResponse']
_CREATEWALLETREQUEST = DESCRIPTOR.message_types_by_name['CreateWalletRequest']
_CREATEWALLETRESPONSE = DESCRIPTOR.message_types_by_name['CreateWalletResponse']
_UNLOCKREQUEST = DESCRIPTOR.message_types_by_name['UnlockRequest']
_UNLOCKRESPONSE = DESCRIPTOR.message_types_by_name['UnlockResponse']
_LOCKREQUEST = DESCRIPTOR.message_types_by_name['LockRequest']
_LOCKRESPONSE = DESCRIPTOR.message_types_by_name['LockResponse']
_CHANGEPASSWORDREQUEST = DESCRIPTOR.message_types_by_name['ChangePasswordRequest']
_CHANGEPASSWORDRESPONSE = DESCRIPTOR.message_types_by_name['ChangePasswordResponse']
_RESTOREWALLETREQUEST = DESCRIPTOR.message_types_by_name['RestoreWalletRequest']
_RESTOREWALLETRESPONSE = DESCRIPTOR.message_types_by_name['RestoreWalletResponse']
_STATUSREQUEST = DESCRIPTOR.message_types_by_name['StatusRequest']
_STATUSRESPONSE = DESCRIPTOR.message_types_by_name['StatusResponse']
_GETINFOREQUEST = DESCRIPTOR.message_types_by_name['GetInfoRequest']
_GETINFORESPONSE = DESCRIPTOR.message_types_by_name['GetInfoResponse']
_GETINFORESPONSE_NETWORK = _GETINFORESPONSE.enum_types_by_name['Network']
GenSeedRequest = _reflection.GeneratedProtocolMessageType('GenSeedRequest', (_message.Message,), {
  'DESCRIPTOR' : _GENSEEDREQUEST,
  '__module__' : 'ocean.v1.wallet_pb2'
  # @@protoc_insertion_point(class_scope:ocean.v1.GenSeedRequest)
  })
_sym_db.RegisterMessage(GenSeedRequest)

GenSeedResponse = _reflection.GeneratedProtocolMessageType('GenSeedResponse', (_message.Message,), {
  'DESCRIPTOR' : _GENSEEDRESPONSE,
  '__module__' : 'ocean.v1.wallet_pb2'
  # @@protoc_insertion_point(class_scope:ocean.v1.GenSeedResponse)
  })
_sym_db.RegisterMessage(GenSeedResponse)

CreateWalletRequest = _reflection.GeneratedProtocolMessageType('CreateWalletRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEWALLETREQUEST,
  '__module__' : 'ocean.v1.wallet_pb2'
  # @@protoc_insertion_point(class_scope:ocean.v1.CreateWalletRequest)
  })
_sym_db.RegisterMessage(CreateWalletRequest)

CreateWalletResponse = _reflection.GeneratedProtocolMessageType('CreateWalletResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATEWALLETRESPONSE,
  '__module__' : 'ocean.v1.wallet_pb2'
  # @@protoc_insertion_point(class_scope:ocean.v1.CreateWalletResponse)
  })
_sym_db.RegisterMessage(CreateWalletResponse)

UnlockRequest = _reflection.GeneratedProtocolMessageType('UnlockRequest', (_message.Message,), {
  'DESCRIPTOR' : _UNLOCKREQUEST,
  '__module__' : 'ocean.v1.wallet_pb2'
  # @@protoc_insertion_point(class_scope:ocean.v1.UnlockRequest)
  })
_sym_db.RegisterMessage(UnlockRequest)

UnlockResponse = _reflection.GeneratedProtocolMessageType('UnlockResponse', (_message.Message,), {
  'DESCRIPTOR' : _UNLOCKRESPONSE,
  '__module__' : 'ocean.v1.wallet_pb2'
  # @@protoc_insertion_point(class_scope:ocean.v1.UnlockResponse)
  })
_sym_db.RegisterMessage(UnlockResponse)

LockRequest = _reflection.GeneratedProtocolMessageType('LockRequest', (_message.Message,), {
  'DESCRIPTOR' : _LOCKREQUEST,
  '__module__' : 'ocean.v1.wallet_pb2'
  # @@protoc_insertion_point(class_scope:ocean.v1.LockRequest)
  })
_sym_db.RegisterMessage(LockRequest)

LockResponse = _reflection.GeneratedProtocolMessageType('LockResponse', (_message.Message,), {
  'DESCRIPTOR' : _LOCKRESPONSE,
  '__module__' : 'ocean.v1.wallet_pb2'
  # @@protoc_insertion_point(class_scope:ocean.v1.LockResponse)
  })
_sym_db.RegisterMessage(LockResponse)

ChangePasswordRequest = _reflection.GeneratedProtocolMessageType('ChangePasswordRequest', (_message.Message,), {
  'DESCRIPTOR' : _CHANGEPASSWORDREQUEST,
  '__module__' : 'ocean.v1.wallet_pb2'
  # @@protoc_insertion_point(class_scope:ocean.v1.ChangePasswordRequest)
  })
_sym_db.RegisterMessage(ChangePasswordRequest)

ChangePasswordResponse = _reflection.GeneratedProtocolMessageType('ChangePasswordResponse', (_message.Message,), {
  'DESCRIPTOR' : _CHANGEPASSWORDRESPONSE,
  '__module__' : 'ocean.v1.wallet_pb2'
  # @@protoc_insertion_point(class_scope:ocean.v1.ChangePasswordResponse)
  })
_sym_db.RegisterMessage(ChangePasswordResponse)

RestoreWalletRequest = _reflection.GeneratedProtocolMessageType('RestoreWalletRequest', (_message.Message,), {
  'DESCRIPTOR' : _RESTOREWALLETREQUEST,
  '__module__' : 'ocean.v1.wallet_pb2'
  # @@protoc_insertion_point(class_scope:ocean.v1.RestoreWalletRequest)
  })
_sym_db.RegisterMessage(RestoreWalletRequest)

RestoreWalletResponse = _reflection.GeneratedProtocolMessageType('RestoreWalletResponse', (_message.Message,), {
  'DESCRIPTOR' : _RESTOREWALLETRESPONSE,
  '__module__' : 'ocean.v1.wallet_pb2'
  # @@protoc_insertion_point(class_scope:ocean.v1.RestoreWalletResponse)
  })
_sym_db.RegisterMessage(RestoreWalletResponse)

StatusRequest = _reflection.GeneratedProtocolMessageType('StatusRequest', (_message.Message,), {
  'DESCRIPTOR' : _STATUSREQUEST,
  '__module__' : 'ocean.v1.wallet_pb2'
  # @@protoc_insertion_point(class_scope:ocean.v1.StatusRequest)
  })
_sym_db.RegisterMessage(StatusRequest)

StatusResponse = _reflection.GeneratedProtocolMessageType('StatusResponse', (_message.Message,), {
  'DESCRIPTOR' : _STATUSRESPONSE,
  '__module__' : 'ocean.v1.wallet_pb2'
  # @@protoc_insertion_point(class_scope:ocean.v1.StatusResponse)
  })
_sym_db.RegisterMessage(StatusResponse)

GetInfoRequest = _reflection.GeneratedProtocolMessageType('GetInfoRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETINFOREQUEST,
  '__module__' : 'ocean.v1.wallet_pb2'
  # @@protoc_insertion_point(class_scope:ocean.v1.GetInfoRequest)
  })
_sym_db.RegisterMessage(GetInfoRequest)

GetInfoResponse = _reflection.GeneratedProtocolMessageType('GetInfoResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETINFORESPONSE,
  '__module__' : 'ocean.v1.wallet_pb2'
  # @@protoc_insertion_point(class_scope:ocean.v1.GetInfoResponse)
  })
_sym_db.RegisterMessage(GetInfoResponse)

_WALLETSERVICE = DESCRIPTOR.services_by_name['WalletService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _GENSEEDREQUEST._serialized_start=57
  _GENSEEDREQUEST._serialized_end=73
  _GENSEEDRESPONSE._serialized_start=75
  _GENSEEDRESPONSE._serialized_end=120
  _CREATEWALLETREQUEST._serialized_start=122
  _CREATEWALLETREQUEST._serialized_end=199
  _CREATEWALLETRESPONSE._serialized_start=201
  _CREATEWALLETRESPONSE._serialized_end=223
  _UNLOCKREQUEST._serialized_start=225
  _UNLOCKREQUEST._serialized_end=268
  _UNLOCKRESPONSE._serialized_start=270
  _UNLOCKRESPONSE._serialized_end=286
  _LOCKREQUEST._serialized_start=288
  _LOCKREQUEST._serialized_end=329
  _LOCKRESPONSE._serialized_start=331
  _LOCKRESPONSE._serialized_end=345
  _CHANGEPASSWORDREQUEST._serialized_start=347
  _CHANGEPASSWORDREQUEST._serialized_end=448
  _CHANGEPASSWORDRESPONSE._serialized_start=450
  _CHANGEPASSWORDRESPONSE._serialized_end=474
  _RESTOREWALLETREQUEST._serialized_start=476
  _RESTOREWALLETREQUEST._serialized_end=602
  _RESTOREWALLETRESPONSE._serialized_start=604
  _RESTOREWALLETRESPONSE._serialized_end=627
  _STATUSREQUEST._serialized_start=629
  _STATUSREQUEST._serialized_end=644
  _STATUSRESPONSE._serialized_start=646
  _STATUSRESPONSE._serialized_end=748
  _GETINFOREQUEST._serialized_start=750
  _GETINFOREQUEST._serialized_end=766
  _GETINFORESPONSE._serialized_start=769
  _GETINFORESPONSE._serialized_end=1261
  _GETINFORESPONSE_NETWORK._serialized_start=1164
  _GETINFORESPONSE_NETWORK._serialized_end=1261
  _WALLETSERVICE._serialized_start=1264
  _WALLETSERVICE._serialized_end=1830
# @@protoc_insertion_point(module_scope)
