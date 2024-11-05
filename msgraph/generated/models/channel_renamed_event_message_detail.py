from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .event_message_detail import EventMessageDetail
    from .identity_set import IdentitySet

from .event_message_detail import EventMessageDetail

@dataclass
class ChannelRenamedEventMessageDetail(EventMessageDetail):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.channelRenamedEventMessageDetail"
    # The updated name of the channel.
    channel_display_name: Optional[str] = None
    # Unique identifier of the channel.
    channel_id: Optional[str] = None
    # Initiator of the event.
    initiator: Optional[IdentitySet] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ChannelRenamedEventMessageDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ChannelRenamedEventMessageDetail
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ChannelRenamedEventMessageDetail()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .event_message_detail import EventMessageDetail
        from .identity_set import IdentitySet

        from .event_message_detail import EventMessageDetail
        from .identity_set import IdentitySet

        fields: Dict[str, Callable[[Any], None]] = {
            "channelDisplayName": lambda n : setattr(self, 'channel_display_name', n.get_str_value()),
            "channelId": lambda n : setattr(self, 'channel_id', n.get_str_value()),
            "initiator": lambda n : setattr(self, 'initiator', n.get_object_value(IdentitySet)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        from .event_message_detail import EventMessageDetail
        from .identity_set import IdentitySet

        writer.write_str_value("channelDisplayName", self.channel_display_name)
        writer.write_str_value("channelId", self.channel_id)
        writer.write_object_value("initiator", self.initiator)
    

