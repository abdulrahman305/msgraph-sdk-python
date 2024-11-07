from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .file_storage import FileStorage
    from .storage_settings import StorageSettings

@dataclass
class Storage(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The fileStorage property
    file_storage: Optional[FileStorage] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The settings property
    settings: Optional[StorageSettings] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Storage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Storage
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Storage()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .file_storage import FileStorage
        from .storage_settings import StorageSettings

        from .file_storage import FileStorage
        from .storage_settings import StorageSettings

        fields: Dict[str, Callable[[Any], None]] = {
            "fileStorage": lambda n : setattr(self, 'file_storage', n.get_object_value(FileStorage)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "settings": lambda n : setattr(self, 'settings', n.get_object_value(StorageSettings)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        from .file_storage import FileStorage
        from .storage_settings import StorageSettings

        writer.write_object_value("fileStorage", self.file_storage)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("settings", self.settings)
        writer.write_additional_data_value(self.additional_data)
    

