from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .conversation_member import ConversationMember

from .conversation_member import ConversationMember

@dataclass
class AnonymousGuestConversationMember(ConversationMember):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.anonymousGuestConversationMember"
    # Unique ID that represents the user. Note: This ID can change if the user leaves and rejoins the meeting, or joins from a different device.
    anonymous_guest_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AnonymousGuestConversationMember:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AnonymousGuestConversationMember
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AnonymousGuestConversationMember()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .conversation_member import ConversationMember

        from .conversation_member import ConversationMember

        fields: Dict[str, Callable[[Any], None]] = {
            "anonymousGuestId": lambda n : setattr(self, 'anonymous_guest_id', n.get_str_value()),
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
        from .conversation_member import ConversationMember

        writer.write_str_value("anonymousGuestId", self.anonymous_guest_id)
    

