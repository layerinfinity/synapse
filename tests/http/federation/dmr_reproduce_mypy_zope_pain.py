from typing import Optional

from zope.interface import Interface, implementer


class IAddress(Interface):
    pass


@implementer(IAddress)
class DummyAddress:
    pass


dummy_address = DummyAddress()


class IProtocol(Interface):
    pass


@implementer(IProtocol)
class Protocol:
    pass


class _WrappingProtocol(Protocol):
    pass


class IProtocolFactory(Interface):
    def buildProtocol(addr: IAddress) -> Optional[IProtocol]:
        pass


def _make_connection(
    client_factory: IProtocolFactory,
) -> None:
    client_protocol = client_factory.buildProtocol(dummy_address)
    assert isinstance(client_protocol, _WrappingProtocol)
    print("Hello")
