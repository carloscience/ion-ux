import datetime

timestamp_created = str(datetime.datetime(2012, 01, 01))
timestamp_updated = str(datetime.datetime.now())

MARINE_FACILITIES_DATA = [

  {'site_id':'abc123', 'information_resource':{'name':'Blue Whale 55', 'description':'A floating buoy'}, 'institution':{'address':'aaa', 'phone':'555-1212', 'email':'example@example.edu', 'website':'http://www.oceanobservatories.org'}, 'contact_information':{'name':'somename', 'address':'123 Main Street', 'city':'San Diego', 'postalcode':'92014', 'phone':'858-555-1212', 'email':'contact@oceanobservatories.org', 'variables':{'name':'var1', 'value':'val1'}}},

  {'site_id':'def123', 'information_resource':{'name':'White Dolphin 1', 'description':'A floating buoy'}, 'institution':{'address':'aaa', 'phone':'555-1212', 'email':'example@example.edu', 'website':'http://www.oceanobservatories.org'}, 'contact_information':{'name':'somename', 'address':'123 Main Street', 'city':'San Diego', 'postalcode':'92014', 'phone':'858-555-1212', 'email':'contact@oceanobservatories.org', 'variables':{'name':'var1', 'value':'val1'}}},

  {'site_id':'hij123', 'information_resource':{'name':'Spiny Lobster 7', 'description':'A floating buoy'}, 'institution':{'address':'aaa', 'phone':'555-1212', 'email':'example@example.edu', 'website':'http://www.oceanobservatories.org'}, 'contact_information':{'name':'somename', 'address':'123 Main Street', 'city':'San Diego', 'postalcode':'92014', 'phone':'858-555-1212', 'email':'contact@oceanobservatories.org', 'variables':{'name':'var1', 'value':'val1'}}},

  {'site_id':'klm123', 'information_resource':{'name':'Spongy Bob 9001', 'description':'A floating buoy'}, 'institution':{'address':'aaa', 'phone':'555-1212', 'email':'example@example.edu', 'website':'http://www.oceanobservatories.org'}, 'contact_information':{'name':'somename', 'address':'123 Main Street', 'city':'San Diego', 'postalcode':'92014', 'phone':'858-555-1212', 'email':'contact@oceanobservatories.org', 'variables':{'name':'var1', 'value':'val1'}}}

]

MARINE_FACILITY_FACEPAGE_DATA = {
    'abc123': {    
        '_id': 'abc123',
        'thumbnail': '/static/img/thumbnail.png',
        'name': 'Blue Whale 55',
        'description': 'Description goes here...',
        'data_products': [
            {'_id': '9028302985', 'name': 'Data Product Alpha', 'dataset_id': '029384023', 'data_product_level': 'High', 'CDM_data_type': 'CDM Data Type', 'ts_updated': timestamp_updated},
            {'_id': '2982309482', 'name': 'Data Product Bravo', 'dataset_id': '029384023', 'data_product_level': 'Low', 'CDM_data_type': 'CDM Data Type', 'ts_updated': timestamp_updated},
            {'_id': '7859827523', 'name': 'Data Product Charlie', 'dataset_id': '029384023', 'data_product_level': 'Medium', 'CDM_data_type': 'CDM Data Type', 'ts_updated': timestamp_updated},
            {'_id': '7501985100', 'name': 'Data Product Delta', 'dataset_id': '029384023', 'data_product_level': 'Insane', 'CDM_data_type': 'CDM Data Type', 'ts_updated': timestamp_updated}
        ],
        'platforms' : [
            {'_id': '1982731982', 'name': 'Zulu Platform', 'description': 'Description goes here...', 'ts_updated': timestamp_updated},
            {'_id': '3456236236', 'name': 'Yankee Plaform', 'description': 'Description goes here...', 'ts_updated': timestamp_updated},
            {'_id': '2474834575', 'name': 'X-Ray Platform', 'description': 'Description goes here...', 'ts_updated': timestamp_updated}
        ],
        'instruments': [
            {'_id': '2891751924', 'name': 'Instrument Whiskey', 'description': 'Description goes here...', 'ts_updated': timestamp_updated},
            {'_id': '9172435345', 'name': 'Instrument Whiskey', 'description': 'Description goes here...', 'ts_updated': timestamp_updated},
            {'_id': '2983479837', 'name': 'Instrument Whiskey', 'description': 'Description goes here...', 'ts_updated': timestamp_updated},
            {'_id': '2394578259', 'name': 'Instrument Whiskey', 'description': 'Description goes here...', 'ts_updated': timestamp_updated}
        ],
        'participants': [
            {'_id': '0298409182', 'name': 'Mike November', 'email': 'mike@november.org', 'description': 'Description goes here...', 'ts_updated': timestamp_updated},
            {'_id': '2394203948', 'name': 'Oscar Papa', 'email': 'oscar@papa.org', 'description': 'Description goes here...', 'ts_updated': timestamp_updated},
            {'_id': '2938429008', 'name': 'Quebec Romeo', 'email': 'quebec@romeo.org', 'description': 'Description goes here...', 'ts_updated': timestamp_updated},
            {'_id': '5569827492', 'name': 'Uniform Victor', 'email': 'uniform@victor.org', 'description': 'Description goes here...', 'ts_updated': timestamp_updated}
        ],
        'events': [
            {'origin': 'Alpha Origin', 'description': 'Description goes here...', 'ts_updated': timestamp_updated},
            {'origin': 'Bravo Origin', 'description': 'Description goes here...', 'ts_updated': timestamp_updated},
            {'origin': 'Charlie Origin', 'description': 'Description goes here...', 'ts_updated': timestamp_updated},
            {'origin': 'Delta Origin', 'description': 'Description goes here...', 'ts_updated': timestamp_updated}
        ],
        'user_requests': [
            {'origin': 'Echo User Request', 'description': 'Description goes here...', 'status': 'Status', 'status_description': 'Status Description', 'user_id': 'User ID', 'type': 'Type', 'ts_updated': timestamp_updated},
            {'origin': 'Foxtrot User Request', 'description': 'Description goes here...', 'status': 'Status', 'status_description': 'Status Description', 'user_id': 'User ID', 'type': 'Type', 'ts_updated': timestamp_updated},
            {'origin': 'Golf User Request', 'description': 'Description goes here...', 'status': 'Status', 'status_description': 'Status Description', 'user_id': 'User ID', 'type': 'Type', 'ts_updated': timestamp_updated},
            {'origin': 'Hotel User Request', 'description': 'Description goes here...', 'status': 'Status', 'status_description': 'Status Description', 'user_id': 'User ID', 'type': 'Type', 'ts_updated': timestamp_updated}
        ],
        'policies': [
            {'name': 'Echo Policy', 'description': 'Description goes here...', 'ts_updated': timestamp_updated},
            {'name': 'Foxtrot Policy', 'description': 'Description goes here...', 'ts_updated': timestamp_updated},
            {'name': 'Golf Policy', 'description': 'Description goes here...', 'ts_updated': timestamp_updated}
        ],
        'instrument_agents': [
            {'_id': '9998409182', 'name': 'Hotel Instrument Agent', 'description': 'Description goes here...', 'driver_model': 'Driver Model', 'client_module': 'Client Module', 'driver_class': 'Driver Class', 'driver_class_client': 'Driver Class Client', 'connection_method': 'Connection Method', 'agent_version': 'Agent Version', 'ts_updated': timestamp_updated},
            {'_id': '2983789274', 'name': 'India Instrument Agent', 'description': 'Description goes here...', 'driver_model': 'Driver Model', 'client_module': 'Client Module', 'driver_class': 'Driver Class', 'driver_class_client': 'Driver Class Client', 'connection_method': 'Connection Method', 'agent_version': 'Agent Version', 'ts_updated': timestamp_updated},
            {'_id': '0981257992', 'name': 'Juliet Instrument Agent', 'description': 'Description goes here...', 'driver_model': 'Driver Model', 'client_module': 'Client Module', 'driver_class': 'Driver Class', 'driver_class_client': 'Driver Class Client', 'connection_method': 'Connection Method', 'agent_version': 'Agent Version', 'ts_updated': timestamp_updated},
            {'_id': '9236289357', 'name': 'Kilo Instrument Agent', 'description': 'Description goes here...', 'driver_model': 'Driver Model', 'client_module': 'Client Module', 'driver_class': 'Driver Class', 'driver_class_client': 'Driver Class Client', 'connection_method': 'Connection Method', 'agent_version': 'Agent Version', 'ts_updated': timestamp_updated}
        ],
        'data_process_defintions': [
            {'_id': '5278293479', 'name': 'Lima Data Process', 'description': 'Description goes here...', 'module': 'Module', 'class_name': 'Class Name', 'process_source': 'Process Source', 'ts_updated': timestamp_updated},
            {'_id': '5289572983', 'name': 'Mike Data Process', 'description': 'Description goes here...', 'module': 'Module', 'class_name': 'Class Name', 'process_source': 'Process Source', 'ts_updated': timestamp_updated},
            {'_id': '2558902959', 'name': 'November Data Process', 'description': 'Description goes here...', 'module': 'Module', 'class_name': 'Class Name', 'process_source': 'Process Source', 'ts_updated': timestamp_updated},
            {'_id': '5235789238', 'name': 'Oscar Data Process', 'description': 'Description goes here...', 'module': 'Module', 'class_name': 'Class Name', 'process_source': 'Process Source', 'ts_updated': timestamp_updated},
        ],
        'platform_models': [
            {'_id': '2375892983', 'name': 'Whiskey Platform Model', 'description': 'Description goes here...', 'manufacturer': 'Manufacturer', 'platform_type': 'Platform Type', 'ooi_node_type': 'OOI Node Type', 'ts_updated': timestamp_updated},
            {'_id': '5892735982', 'name': 'X-Ray Platform Model', 'description': 'Description goes here...', 'manufacturer': 'Manufacturer', 'platform_type': 'Platform Type', 'ooi_node_type': 'OOI Node Type', 'ts_updated': timestamp_updated},
            {'_id': '2837587293', 'name': 'Yankee Platform Model', 'description': 'Description goes here...', 'manufacturer': 'Manufacturer', 'platform_type': 'Platform Type', 'ooi_node_type': 'OOI Node Type', 'ts_updated': timestamp_updated},
            {'_id': '5789234922', 'name': 'Zulu Platform Model', 'description': 'Description goes here...', 'manufacturer': 'Manufacturer', 'platform_type': 'Platform Type', 'ooi_node_type': 'OOI Node Type', 'ts_updated': timestamp_updated},
        ],
        'instrument_models': [
            {'_id': '4592038490', 'name': 'Alpha Bravo Instrument Model', 'description': 'Description goes here...', 'model_label': 'Model Label', 'manufacturer': 'Manufacturer', 'instrument_family': 'Instrument Family', 'instrument_class': 'Instrument Class', 'primary_interface': 'Primary Interface', 'ts_updated': timestamp_updated},
            {'_id': '7589273493', 'name': 'Charle Delta Instrument Model', 'description': 'Description goes here...', 'model_label': 'Model Label', 'manufacturer': 'Manufacturer', 'instrument_family': 'Instrument Family', 'instrument_class': 'Instrument Class', 'primary_interface': 'Primary Interface', 'ts_updated': timestamp_updated},
            {'_id': '5678969843', 'name': 'Echo Foxtrot Instrument Model', 'description': 'Description goes here...', 'model_label': 'Model Label', 'manufacturer': 'Manufacturer', 'instrument_family': 'Instrument Family', 'instrument_class': 'Instrument Class', 'primary_interface': 'Primary Interface', 'ts_updated': timestamp_updated},
            {'_id': '1812739873', 'name': 'Golf Hotel Instrument Model', 'description': 'Description goes here...', 'model_label': 'Model Label', 'manufacturer': 'Manufacturer', 'instrument_family': 'Instrument Family', 'instrument_class': 'Instrument Class', 'primary_interface': 'Primary Interface', 'ts_updated': timestamp_updated}
        ],
        'frames_of_reference': [
            {'_id': '2987594835', 'name': 'Site Bravo', 'owner': 'John Doe', 'type': 'Type','ts_updated': timestamp_updated},
            {'_id': '5346466644', 'name': 'Site Alpha', 'owner': 'Jane Doe', 'type': 'Type','ts_updated': timestamp_updated},
            {'_id': '3463636777', 'name': 'Site Charlie', 'owner': 'John Doe', 'type': 'Type', 'ts_updated': timestamp_updated},
            {'_id': '3453454366', 'name': 'Site Delta', 'description': 'Jane Doe', 'type': 'Type', 'ts_updated': timestamp_updated},        
        ]
    }, 
}


PLATFORM_FACEPAGE_DATA = {
    '1982731982': { 
        '_id': '1982731982',
        'thumbnail': '/static/img/thumbnail.png',
        'name': 'North by Northwest',
        'model': 'Model',
        'serial': '1234567890',
        'manufacture_date': timestamp_updated,
        'description': 'Description goes here...',
        'manufacturer': 'Manufacturer',
        'owner': 'Owner',
        'agents': [
            {'_id': '769872987', 'name': 'Alpha Agent', 'description': 'Description goes here...', 'configuration': 'Configuration goes here...'},
            {'_id': '769872987', 'name': 'Bravo Agent', 'description': 'Description goes here...', 'configuration': 'Configuration goes here...'},
            {'_id': '769872987', 'name': 'Charlie Agent', 'description': 'Description goes here...', 'configuration': 'Configuration goes here...'},
            {'_id': '769872987', 'name': 'Delta Agent', 'description': 'Description goes here...', 'configuration': 'Configuration goes here...'}
        ],
        'policies': [
            {'name': 'Echo Policy', 'description': 'Description goes here...', 'ts_updated': timestamp_updated},
            {'name': 'Foxtrot Policy', 'description': 'Description goes here...', 'ts_updated': timestamp_updated},
            {'name': 'Golf Policy', 'description': 'Description goes here...', 'ts_updated': timestamp_updated}
        ],
        'instruments': [
            {'_id': '2891751924', 'name': 'Instrument Whiskey', 'description': 'Description goes here...', 'ts_updated': timestamp_updated},
            {'_id': '9172435345', 'name': 'Instrument Whiskey', 'description': 'Description goes here...', 'ts_updated': timestamp_updated},
            {'_id': '2983479837', 'name': 'Instrument Whiskey', 'description': 'Description goes here...', 'ts_updated': timestamp_updated},
            {'_id': '2394578259', 'name': 'Instrument Whiskey', 'description': 'Description goes here...', 'ts_updated': timestamp_updated}
        ],
        'events': [
            {'origin': 'Alpha Origin', 'description': 'Description goes here...', 'ts_updated': timestamp_updated},
            {'origin': 'Bravo Origin', 'description': 'Description goes here...', 'ts_updated': timestamp_updated},
            {'origin': 'Charlie Origin', 'description': 'Description goes here...', 'ts_updated': timestamp_updated},
            {'origin': 'Delta Origin', 'description': 'Description goes here...', 'ts_updated': timestamp_updated}
        ],
        'user_requests': [
            {'origin': 'Echo User Request', 'description': 'Description goes here...', 'status': 'Status', 'status_description': 'Status Description', 'user_id': 'User ID', 'type': 'Type', 'ts_updated': timestamp_updated},
            {'origin': 'Foxtrot User Request', 'description': 'Description goes here...', 'status': 'Status', 'status_description': 'Status Description', 'user_id': 'User ID', 'type': 'Type', 'ts_updated': timestamp_updated},
            {'origin': 'Golf User Request', 'description': 'Description goes here...', 'status': 'Status', 'status_description': 'Status Description', 'user_id': 'User ID', 'type': 'Type', 'ts_updated': timestamp_updated},
            {'origin': 'Hotel User Request', 'description': 'Description goes here...', 'status': 'Status', 'status_description': 'Status Description', 'user_id': 'User ID', 'type': 'Type', 'ts_updated': timestamp_updated}
        ]
    },
}

INSTRUMENT_FACEPAGE_DATA = {
  "data": {
    "data_products": [
      {
        "lcstate": "DEPLOYED_AVAILABLE", 
        "_rev": "3-af4c9dff22fd6142867a6d5493a6ca7d", 
        "keywords": {}, 
        "iso_topic_category": "", 
        "version_status": "active", 
        "ts_created": "1343865460188", 
        "dataset_configuration_id": "191c539acfc24100bb70272d5bdbfe6f", 
        "geospatial_bounds": {
          "geospatialverticalmin": 0.0, 
          "geospatiallonresolution": 0.0, 
          "geospatiallatunits": "", 
          "geospatiallatmin": 44.55, 
          "geospatialverticalunits": "", 
          "type_": "GeospatialBounds", 
          "geospatialverticalmax": 0.0, 
          "geospatiallonunits": "", 
          "maxbottomdepth": 205.0, 
          "geospatialverticalresolution": 0.0, 
          "geospatiallatmax": 44.65, 
          "geospatiallonmin": -125.45, 
          "minbottomdepth": 0.0, 
          "geospatiallatresolution": 0.0, 
          "geospatiallonmax": -125.35, 
          "depthverticalpositive": 0.0, 
          "geospatialverticalpositive": 0.0, 
          "depthunits": ""
        }, 
        "data_url": "", 
        "description": "Raw stream from SBE37 simulator Replacement", 
        "ISO_spatial_representation_type": "textTable", 
        "processing_level_code": "Raw", 
        "ts_updated": "1343865461137", 
        "quality_control_level": "a", 
        "exclusive_rights_status": "Public", 
        "point_of_contact_list": [], 
        "name": "CTDBP-1012-REC1 Raw Endurance OR Offshore Benthic Pkg Demo Replacement", 
        "acknowledgement": "", 
        "data_format": {
          "format_version_identifier": "", 
          "name": "", 
          "description": "", 
          "type_": "DataFormat", 
          "character_set": "", 
          "long_name": "", 
          "between_record_delimiter": "", 
          "nominal_sampling_rate_maximum": "", 
          "unique_short_name": "", 
          "units": "", 
          "missing_value": "", 
          "nominal_sampling_rate_minimum": "", 
          "value_format": ""
        }, 
        "iso_spatial_representation_type": "", 
        "license_uri": "", 
        "type_": "DataProduct", 
        "CDM_data_type": "station", 
        "_id": "262892cca7944e79bb71231d9af1cd6b"
      }, 
      {
        "lcstate": "DEPLOYED_AVAILABLE", 
        "_rev": "3-31e6b93f7cb3aa24125d3995acc1dd7d", 
        "keywords": {}, 
        "iso_topic_category": "", 
        "version_status": "active", 
        "ts_created": "1343865461161", 
        "dataset_configuration_id": "191c539acfc24100bb70272d5bdbfe6f", 
        "geospatial_bounds": {
          "geospatialverticalmin": 0.0, 
          "geospatiallonresolution": 0.0, 
          "geospatiallatunits": "", 
          "geospatiallatmin": 44.5, 
          "geospatialverticalunits": "", 
          "type_": "GeospatialBounds", 
          "geospatialverticalmax": 0.0, 
          "geospatiallonunits": "", 
          "maxbottomdepth": 3000.0, 
          "geospatialverticalresolution": 0.0, 
          "geospatiallatmax": 44.7, 
          "geospatiallonmin": -125.5, 
          "minbottomdepth": 0.0, 
          "geospatiallatresolution": 0.0, 
          "geospatiallonmax": -125.3, 
          "depthverticalpositive": 0.0, 
          "geospatialverticalpositive": 0.0, 
          "depthunits": ""
        }, 
        "data_url": "", 
        "description": "Parsed Stream from SBE37 simulator Replacement", 
        "ISO_spatial_representation_type": "textTable", 
        "processing_level_code": "Parsed_Canonical", 
        "ts_updated": "1343865462412", 
        "quality_control_level": "a", 
        "exclusive_rights_status": "Public", 
        "point_of_contact_list": [], 
        "name": "CTDBP-1012-REC1 Parsed Endurance OR Offshore Benthic Pkg Demo Replacement", 
        "acknowledgement": "", 
        "data_format": {
          "format_version_identifier": "", 
          "name": "", 
          "description": "", 
          "type_": "DataFormat", 
          "character_set": "", 
          "long_name": "", 
          "between_record_delimiter": "", 
          "nominal_sampling_rate_maximum": "", 
          "unique_short_name": "", 
          "units": "", 
          "missing_value": "", 
          "nominal_sampling_rate_minimum": "", 
          "value_format": ""
        }, 
        "iso_spatial_representation_type": "", 
        "license_uri": "", 
        "type_": "DataProduct", 
        "CDM_data_type": "station", 
        "_id": "7872c89861e84aeaa8178b26da8d4084"
      }
    ], 
    "resource": {
      "controllable": true, 
      "description": "Simulator 2 replacement for 1 providing CTD data in the LCA demonstration", 
      "lot_number": "", 
      "_rev": "3-2b602b46d0480d2f6291bbf4e5d36372", 
      "name": "CTD Simulator 2 Demo", 
      "ts_updated": "1343865443386", 
      "type_": "InstrumentDevice", 
      "serial_number": "10004", 
      "has_platform_position": "", 
      "firmware_version": "0-00", 
      "_id": "d1113adf551d4196a656b54a63900611", 
      "ts_created": "1343865443059", 
      "manufacture_date": "", 
      "lcstate": "DEPLOYED_AVAILABLE"
    }, 
    "attachments": [
      {
        "lcstate": "DEPLOYED_AVAILABLE", 
        "_rev": "1-c9fbdc6abe40fa8e743998f81cb261fa", 
        "object_id": "d1113adf551d4196a656b54a63900611", 
        "name": "", 
        "content": "", 
        "ts_updated": "1343865473705", 
        "type_": "Attachment", 
        "content_type": "text/csv", 
        "keywords": [], 
        "_id": "510e29c1ed084584af5601cf72abc5b3", 
        "ts_created": "1343865473705", 
        "attachment_type": 1, 
        "description": ""
      }
    ], 
    "instrument_agent": {
      "description": "CTD Instrument Agent", 
      "name": "CTD Instrument Agent Demo", 
      "driver_client_module": "", 
      "ts_created": "1343865445139", 
      "_rev": "3-0c5e6fb68e2fe50358f22bf3688e0dd3", 
      "driver_class": "InstrumentAgent", 
      "type_": "InstrumentAgent", 
      "time_source": "", 
      "agent_version": "0.1", 
      "event_publisher_origin": "", 
      "ts_updated": "1343865445429", 
      "conection_method": "", 
      "driver_module": "ion.agents.instrument.instrument_agent", 
      "_id": "4b866a07a58f48249bd445ad8b457001", 
      "driver_class_client": "", 
      "lcstate": "DEPLOYED_AVAILABLE"
    }, 
    "owners": [
      {
        "lcstate": "DEPLOYED_AVAILABLE", 
        "_rev": "1-fc9353956cddfcf2f06ec33660807cea", 
        "name": "", 
        "ts_updated": "1343865424836", 
        "type_": "UserInfo", 
        "contact": {
          "city": "", 
          "first_name": "", 
          "name": "Owen Ownerrep", 
          "country": "", 
          "variables": [
            {
              "name": "", 
              "value": ""
            }
          ], 
          "type_": "ContactInformation", 
          "phone": "", 
          "state": "", 
          "address": "", 
          "postalcode": "", 
          "email": "owenownerrep@gmail.com"
        }, 
        "_id": "ae759ae3f00540ebb83e70780118c8f1", 
        "ts_created": "1343865424836", 
        "variables": [
          {
            "name": "", 
            "value": ""
          }
        ], 
        "description": ""
      }
    ], 
    "instrument_model": {
      "lcstate": "DEPLOYED_AVAILABLE", 
      "weight": 0.0, 
      "manufacturer_url": "", 
      "wattage": 0.0, 
      "mixed_sampling_mode": true, 
      "hotel_current": "", 
      "height": 0.0, 
      "voltage": 0.0, 
      "baud_rate_default": "", 
      "integrated_inductive_modem_available": true, 
      "internal_battery": true, 
      "length": 0.0, 
      "width": 0.0, 
      "clock_notes": "None", 
      "internal_data_storage": true, 
      "operational_depth_maximum": 0.0, 
      "electrical_notes": "", 
      "_rev": "1-814197b6198dbd285e7d4a8525f59487", 
      "survival_depth_maximum": 0.0, 
      "description": "A Sea-bird conductivity and temperature (pressure optional) recorder (CTD) model designed for moorings or other long duration, fixed-site deployments.", 
      "instrument_family": "CTD", 
      "inline_management": true, 
      "ts_updated": "1343865437141", 
      "primary_interface": "", 
      "operational_temperature_range": "", 
      "power_supply_voltage_maximum": 0.0, 
      "ts_created": "1343865437141", 
      "clock_max_drift": 0.0, 
      "name": "SBE 37-SMP MicroCAT CTD Model Demo", 
      "required_ontime": "", 
      "reference_url": "http://www.seabird.com/pdf_documents/manuals/37SMP_RS232_016.pdf, http://www.seabird.com/products/spec_sheets/37smpdata.htm", 
      "type_": "InstrumentModel", 
      "power_supply_voltage_minimum": 0.0, 
      "power_source": "", 
      "model": "", 
      "_id": "75f498f62e4e419895fb38e9c8effb92"
    }, 
    "platform_device": {
      "controllable": true, 
      "lcstate": "DRAFT_PRIVATE", 
      "nominal_location": {
        "lat": 0.0, 
        "type_": "GeospatialLocation", 
        "lon": 0.0
      }, 
      "name": "", 
      "ts_updated": "", 
      "type_": "PlatformDevice", 
      "platform_family": "", 
      "serial_number": "", 
      "ts_created": "", 
      "description": ""
    }, 
    "type_": "InstrumentDeviceExtension", 
    "sensor_devices": [], 
    "policies": [], 
    "ext_associations": {}, 
    "_id": "d1113adf551d4196a656b54a63900611", 
    "ts_created": "1343942511667", 
    "platform_model": {
      "ci_onboard": "", 
      "lcstate": "DRAFT_PRIVATE", 
      "weight": 0.0, 
      "platform_type": "", 
      "OOI_node_type": "", 
      "manufacturer_url": "", 
      "wattage": 0.0, 
      "maximum_crew": 0, 
      "height": 0.0, 
      "shore_networked": true, 
      "width": 0.0, 
      "length": 0.0, 
      "voltage": 0.0, 
      "type_": "PlatformModel", 
      "model": "", 
      "ts_updated": "", 
      "ts_created": "", 
      "name": "", 
      "description": ""
    }, 
    "computed": {
      "last_command_date": "45", 
      "communications_status_roll_up": "89", 
      "last_data_received_time": "42", 
      "type_": "InstrumentDeviceComputedAttributes", 
      "operational_state": "23", 
      "last_command_status": "34", 
      "last_command": "56", 
      "last_commanded_by": "67", 
      "power_status_roll_up": "78", 
      "location": {
        "geospatialverticalmin": 0.0, 
        "geospatiallonresolution": 0.0, 
        "geospatiallatunits": "", 
        "geospatiallatmin": 0.0, 
        "geospatialverticalunits": "", 
        "type_": "GeospatialBounds", 
        "geospatialverticalmax": 0.0, 
        "geospatiallonunits": "", 
        "maxbottomdepth": 0.0, 
        "geospatialverticalresolution": 0.0, 
        "geospatiallatmax": 0.0, 
        "geospatiallonmin": 0.0, 
        "minbottomdepth": 0.0, 
        "geospatiallatresolution": 0.0, 
        "geospatiallonmax": 0.0, 
        "depthverticalpositive": 0.0, 
        "geospatialverticalpositive": 0.0, 
        "depthunits": ""
      }, 
      "data_status_roll_up": "98", 
      "firmware_version": "1.1", 
      "location_status_roll_up": "87", 
      "recent_events": [
        "mon", 
        "tue", 
        "wed"
      ]
    }
  }
}


DATA = {
    "data_resource_id": "3319A67F-81F3-424F-8E69-4F28C4E0AAAA",
    "source":{"request_type": "DAP","base_url": "http://geoport.whoi.edu/thredds/dodsC/usgs/data0/rsignell/data/oceansites/OS_NTAS_2010_R_M-1.nc","max_ingest_millis": 6000,"ion_title": "NTAS1 Data Source","ion_description": "Data NTAS1","ion_name": "MyOOICI","ion_email": "myooici@gmail.com","ion_institution": "OOICI"},
    "variable": [{"units": "degree_north","standard_name": "latitude","long_name": "northward positive degrees latitude"},{"units": "degree_east","standard_name": "longitude","long_name": "eastward positive degrees longitude"},{"standard_name": "station_id","long_name": "integer station identifier"},{"units": "psu","standard_name": "sea_water_salinity","long_name": "water salinity at location","other_attributes": ["coordinates=time lon lat z"]},{"units": "seconds since 1970-01-01 00:00::00","standard_name": "time","long_name": "time","other_attributes": ["_CoordinateAxisType=Time"]},{"units": "m","standard_name": "depth","long_name": "depth below mean sea level","other_attributes": ["positive=down","::_CoordinateAxisType=Height","::_CoordinateZisPositive=down"]}],

"variable": [{"standard_name": "station_id","name": "stnId"}, {"units": "degree_east","standard_name": "longitude - here is some really long testing text...","long_name": "longitude","name": "lon","other_attributes": [{"name": "_CoordinateAxisType","value": "Lon"}]}, {"units": "seconds since 1970-01-01 00:00:00","standard_name": "time","long_name": "time","name": "time","other_attributes": [{"name": "_CoordinateAxisType","value": "Time"}],"dimensions": [{"name": "time","length": 947.0}]}, {"units": "m","standard_name": "depth","long_name": "depth below mean sea level","name": "z","other_attributes": [{"name": "positive","value": "down"},{"name": "missing_value","value": "-9999.0"},{"name": "_CoordinateAxisType","value": "Height"},{"name": "_CoordinateZisPositive","value": "down"}]}, {"units": "ft","standard_name": "precipitation_total","long_name": "total precipitation at gauge location in feet","name": "precipitation_total","other_attributes": [{"name": "coordinates","value": "time lon lat"}],"dimensions": [{"name": "time","length": 947.0}, {"name": "height","length": 111.0}]}],

"dimensions": [{"name": "time","length": 947.0}, {"name": "height","length": 111.0}],

"other_attributes": [{"name": "CF:featureType","value": "station"},{"name": "Conventions","value": "CF-1.5"},{"name": "history","value": "Converted from WaterML1.1 to OOI CDM by net.ooici.eoi.datasetagent.impl.UsgsAgent"}]


}


ALL_RESOURCES_DATA = [{"datasetMetadata":{"summary":"Near-real-time surface data from ASIMet system 1 on the seventh deployment of the WHOI HOT Station (WHOTS) observatory.","ion_geospatial_lon_min":-158,"ion_geospatial_lon_max":-158,"ion_time_coverage_start":"2011-06-20T20:00:00Z","ion_geospatial_vertical_max":0,"ion_geospatial_vertical_min":0,"title":"WHOTS 7 near-real-time Mooring Data, System 1","references":"http:// www.oceansites.org, http://uop.whoi.edu/projects/whots","user_ooi_id":"Is this used?","source":"Mooring observation","ion_time_coverage_end":"2011-06-21T15:59:59Z","ion_geospatial_lat_max":22.75,"download_url":"http://thredds.oceanobservatories.org/thredds/dodsC/ooiciData/7EF91B33-6784-4BE6-B014-ACEEA2BFFF3D.ncml.html","data_resource_id":"7EF91B33-6784-4BE6-B014-ACEEA2BFFF3D","ion_geospatial_lat_min":22.75,"ion_geospatial_vertical_positive":"down","comment":"Argos, hourly averaged ASIMet data","institution":"WHOI"},"notificationSet":False,"date_registered":1308686653471},{"datasetMetadata":{"ion_geospatial_lon_min":-74.8399963379,"ion_geospatial_lon_max":-74.8399963379,"ion_time_coverage_start":"2011-06-16T00:50:00Z","ion_geospatial_vertical_max":-5,"ion_geospatial_vertical_min":-5,"title":"SOS (urn:ioos:station:wmo:44014) Winds","references":"http://sdf.ndbc.noaa.gov/sos/ , http://example.edu/second-url-test","user_ooi_id":"Is this used?","source":"Sensor Observation Service (http://sdf.ndbc.noaa.gov/sos/server.php?)","ion_time_coverage_end":"2011-06-16T23:50:00Z","ion_geospatial_lat_max":36.6100006104,"download_url":"http://thredds.oceanobservatories.org/thredds/dodsC/ooiciData/871CE078-9676-4D55-931B-1C3A4022E859.ncml.html","data_resource_id":"871CE078-9676-4D55-931B-1C3A4022E859","ion_geospatial_lat_min":36.6100006104,"ion_geospatial_vertical_positive":"down","institution":"NOAA NDBC"},"notificationSet":False,"date_registered":1308269073544},{"datasetMetadata":{"ion_geospatial_lon_min":-74.8399963379,"ion_geospatial_lon_max":-74.8399963379,"ion_time_coverage_start":"2011-06-20T20:50:00Z","ion_geospatial_vertical_max":3.79999995232,"ion_geospatial_vertical_min":3.79999995232,"title":"SOS (urn:ioos:station:wmo:44014) Currents","references":"http://sdf.ndbc.noaa.gov/sos/ , http://example.edu/second-url-test","user_ooi_id":"Is this used?","source":"Sensor Observation Service (http://sdf.ndbc.noaa.gov/sos/server.php?)","ion_time_coverage_end":"2011-06-21T20:50:00Z","ion_geospatial_lat_max":36.6100006104,"download_url":"http://thredds.oceanobservatories.org/thredds/dodsC/ooiciData/65851927-E263-4809-B022-94AF0562F77D.ncml.html","data_resource_id":"65851927-E263-4809-B022-94AF0562F77D","ion_geospatial_lat_min":36.6100006104,"ion_geospatial_vertical_positive":"down","institution":"NOAA NDBC"},"notificationSet":True,"date_registered":1308686672556},{"datasetMetadata":{"ion_geospatial_lon_min":-72.6053695679,"ion_geospatial_lon_max":-72.6053695679,"ion_time_coverage_start":"2011-06-19T20:15:00Z","ion_geospatial_vertical_max":0,"ion_geospatial_vertical_min":0,"title":"CONNECTICUT RIVER AT THOMPSONVILLE CT (01184000) - Instantaneous Value","references":"http://waterservices.usgs.gov/rest/WOF-IV-Service.html","user_ooi_id":"Is this used?","source":"Instantaneous Values Webservice (http://waterservices.usgs.gov/mwis/iv?)","ion_time_coverage_end":"2011-06-21T19:45:00Z","ion_geospatial_lat_max":41.9873199463,"download_url":"http://thredds.oceanobservatories.org/thredds/dodsC/ooiciData/50B9D322-F80A-4271-925C-B91EBC66C19E.ncml.html","data_resource_id":"50B9D322-F80A-4271-925C-B91EBC66C19E","ion_geospatial_lat_min":41.9873199463,"ion_geospatial_vertical_positive":"down","institution":"USGS NWIS"},"notificationSet":True,"date_registered":1308686643570},{"datasetMetadata":{"summary":"Real-time surface data from ASIMet system 2 on the tenth Northwest Tropcial Stlantic Station (NTAS) observatory.","ion_geospatial_lon_min":-51,"ion_geospatial_lon_max":-51,"ion_time_coverage_start":"2011-06-20T20:00:00Z","ion_geospatial_vertical_max":0,"ion_geospatial_vertical_min":0,"title":"NTAS 10 Real-time Mooring Data, System 2","references":"http:// www.oceansites.org, http://uop.whoi.edu/projects/ntas","user_ooi_id":"Is this used?","source":"Mooring observation","ion_time_coverage_end":"2011-06-21T15:59:59Z","ion_geospatial_lat_max":15,"download_url":"http://thredds.oceanobservatories.org/thredds/dodsC/ooiciData/FFC86EFE-4918-49D2-9E30-8689581A7715.ncml.html","data_resource_id":"FFC86EFE-4918-49D2-9E30-8689581A7715","ion_geospatial_lat_min":15,"ion_geospatial_vertical_positive":"down","comment":"Argos, hourly averaged ASIMet data","institution":"WHOI"},"notificationSet":False,"date_registered":1308686624444},{"datasetMetadata":{"summary":"Near-real-time surface data from ASIMet system 1 on the seventh deployment of the WHOI HOT Station (WHOTS) observatory.","ion_geospatial_lon_min":-158,"ion_geospatial_lon_max":-158,"ion_time_coverage_start":"2011-06-20T20:00:00Z","ion_geospatial_vertical_max":0,"ion_geospatial_vertical_min":0,"title":"WHOTS 7 near-real-time Mooring Data, System 1","references":"http:// www.oceansites.org, http://uop.whoi.edu/projects/whots","user_ooi_id":"Is this used?","source":"Mooring observation","ion_time_coverage_end":"2011-06-21T15:59:59Z","ion_geospatial_lat_max":22.75,"download_url":"http://thredds.oceanobservatories.org/thredds/dodsC/ooiciData/57CDE283-2066-4107-9CD7-DD11BD1B83BB.ncml.html","data_resource_id":"57CDE283-2066-4107-9CD7-DD11BD1B83BB","ion_geospatial_lat_min":22.75,"ion_geospatial_vertical_positive":"down","comment":"Argos, hourly averaged ASIMet data","institution":"WHOI"},"notificationSet":False,"date_registered":1308686648713},{"datasetMetadata":{"summary":"Real-time surface data from ASIMet system 1 on the tenth Northwest Tropcial Stlantic Station (NTAS) observatory.","ion_geospatial_lon_min":-51,"ion_geospatial_lon_max":-51,"ion_time_coverage_start":"2011-06-15T23:00:00Z","ion_geospatial_vertical_max":0,"ion_geospatial_vertical_min":0,"title":"NTAS 10 Real-time Mooring Data, System 1","references":"http:// www.oceansites.org, http://uop.whoi.edu/projects/ntas","user_ooi_id":"Is this used?","source":"Mooring observation","ion_time_coverage_end":"2011-06-16T21:59:59Z","ion_geospatial_lat_max":15,"download_url":"http://thredds.oceanobservatories.org/thredds/dodsC/ooiciData/8F443AC7-B999-4F49-B4F1-B737BF07E167.ncml.html","data_resource_id":"8F443AC7-B999-4F49-B4F1-B737BF07E167","ion_geospatial_lat_min":15,"ion_geospatial_vertical_positive":"down","comment":"Argos, hourly averaged ASIMet data","institution":"WHOI"},"notificationSet":False,"date_registered":1308265819914},{"datasetMetadata":{"summary":"Near-real-time surface data from ASIMet system 2 on the seventh deployment of the WHOI HOT Station (WHOTS) observatory.","ion_geospatial_lon_min":-158,"ion_geospatial_lon_max":-158,"ion_time_coverage_start":"2011-06-20T20:00:00Z","ion_geospatial_vertical_max":0,"ion_geospatial_vertical_min":0,"title":"WHOTS 7 near-real-time Mooring Data, System 2","references":"http:// www.oceansites.org, http://uop.whoi.edu/projects/whots","user_ooi_id":"Is this used?","source":"Mooring observation","ion_time_coverage_end":"2011-06-21T14:00:00Z","ion_geospatial_lat_max":22.75,"download_url":"http://thredds.oceanobservatories.org/thredds/dodsC/ooiciData/D56B7445-BED7-4F23-9F9F-E05BC07A8618.ncml.html","data_resource_id":"D56B7445-BED7-4F23-9F9F-E05BC07A8618","ion_geospatial_lat_min":22.75,"ion_geospatial_vertical_positive":"down","comment":"Argos, hourly averaged ASIMet data","institution":"WHOI"},"notificationSet":False,"date_registered":1308686663068},{"datasetMetadata":{"ion_geospatial_lon_min":-74.8399963379,"ion_geospatial_lon_max":-74.8399963379,"ion_time_coverage_start":"2011-06-20T20:50:00Z","ion_geospatial_vertical_max":-5,"ion_geospatial_vertical_min":-5,"title":"SOS (urn:ioos:station:wmo:44014) Winds","references":"http://sdf.ndbc.noaa.gov/sos/, http://example.edu/second-url-test","user_ooi_id":"Is this used?","source":"Sensor Observation Service (http://sdf.ndbc.noaa.gov/sos/server.php?)","ion_time_coverage_end":"2011-06-21T19:50:00Z","ion_geospatial_lat_max":36.6100006104,"download_url":"http://thredds.oceanobservatories.org/thredds/dodsC/ooiciData/78776F15-0193-45E3-921C-44597D32F8F9.ncml.html","data_resource_id":"78776F15-0193-45E3-921C-44597D32F8F9","ion_geospatial_lat_min":36.6100006104,"ion_geospatial_vertical_positive":"down","institution":"NOAA NDBC"},"notificationSet":False,"date_registered":1308686658126},{"datasetMetadata":{"summary":"Real-time surface data from ASIMet system 1 on the tenth Northwest Tropcial Stlantic Station (NTAS) observatory.","ion_geospatial_lon_min":-51,"ion_geospatial_lon_max":-51,"ion_time_coverage_start":"2011-06-20T20:00:00Z","ion_geospatial_vertical_max":0,"ion_geospatial_vertical_min":0,"title":"NTAS 10 Real-time Mooring Data, System 1","references":"http:// www.oceansites.org, http://uop.whoi.edu/projects/ntas","user_ooi_id":"Is this used?","source":"Mooring observation","ion_time_coverage_end":"2011-06-21T15:59:59Z","ion_geospatial_lat_max":15,"download_url":"http://thredds.oceanobservatories.org/thredds/dodsC/ooiciData/51D20C92-88D1-4D06-BD75-9C7654FE5EC1.ncml.html","data_resource_id":"51D20C92-88D1-4D06-BD75-9C7654FE5EC1","ion_geospatial_lat_min":15,"ion_geospatial_vertical_positive":"down","comment":"Argos, hourly averaged ASIMet data","institution":"WHOI"},"notificationSet":True,"date_registered":1308686607700},{"datasetMetadata":{"ion_geospatial_lon_min":-72.6053695679,"ion_geospatial_lon_max":-72.6053695679,"ion_time_coverage_start":"2011-06-15T23:45:00Z","ion_geospatial_vertical_max":0,"ion_geospatial_vertical_min":0,"title":"CONNECTICUT RIVER AT THOMPSONVILLE CT (01184000) - Instantaneous Value","references":"http://waterservices.usgs.gov/rest/WOF-IV-Service.html","user_ooi_id":"Is this used?","source":"Instantaneous Values Webservice (http://waterservices.usgs.gov/mwis/iv?)","ion_time_coverage_end":"2011-06-17T22:30:00Z","ion_geospatial_lat_max":41.9873199463,"download_url":"http://thredds.oceanobservatories.org/thredds/dodsC/ooiciData/D777193D-A6D9-49D5-91FA-58D980446164.ncml.html","data_resource_id":"D777193D-A6D9-49D5-91FA-58D980446164","ion_geospatial_lat_min":41.9873199463,"ion_geospatial_vertical_positive":"down","institution":"USGS NWIS"},"notificationSet":False,"date_registered":1308353849228},{"datasetMetadata":{"summary":"Real-time surface data from ASIMet system 2 on the tenth Northwest Tropcial Stlantic Station (NTAS) observatory.","ion_geospatial_lon_min":-51,"ion_geospatial_lon_max":-51,"ion_time_coverage_start":"2011-06-20T20:00:00Z","ion_geospatial_vertical_max":0,"ion_geospatial_vertical_min":0,"title":"NTAS 10 Real-time Mooring Data, System 2","references":"http:// www.oceansites.org, http://uop.whoi.edu/projects/ntas","user_ooi_id":"Is this used?","source":"Mooring observation","ion_time_coverage_end":"2011-06-21T15:59:59Z","ion_geospatial_lat_max":15,"download_url":"http://thredds.oceanobservatories.org/thredds/dodsC/ooiciData/679222D7-C661-407C-9483-951DF66D2038.ncml.html","data_resource_id":"679222D7-C661-407C-9483-951DF66D2038","ion_geospatial_lat_min":15,"ion_geospatial_vertical_positive":"down","comment":"Argos, hourly averaged ASIMet data","institution":"WHOI"},"notificationSet":False,"date_registered":1308686619252},{"datasetMetadata":{"ion_geospatial_lon_min":-74.8399963379,"ion_geospatial_lon_max":-74.8399963379,"ion_time_coverage_start":"2011-06-20T20:50:00Z","ion_geospatial_vertical_max":-4,"ion_geospatial_vertical_min":-4,"title":"SOS (urn:ioos:station:wmo:44014) air_temperature","references":"http://sdf.ndbc.noaa.gov/sos/, http://example.edu/second-url-test","user_ooi_id":"Is this used?","source":"Sensor Observation Service (http://sdf.ndbc.noaa.gov/sos/server.php?)","ion_time_coverage_end":"2011-06-21T19:50:00Z","ion_geospatial_lat_max":36.6100006104,"download_url":"http://thredds.oceanobservatories.org/thredds/dodsC/ooiciData/417AD47D-98F9-4EE9-AAA8-8C4B19915DDE.ncml.html","data_resource_id":"417AD47D-98F9-4EE9-AAA8-8C4B19915DDE","ion_geospatial_lat_min":36.6100006104,"ion_geospatial_vertical_positive":"down","institution":"NOAA NDBC"},"notificationSet":True,"date_registered":1308686667919},{"datasetMetadata":{"summary":"Real-time surface data from ASIMet system 1 on the tenth Northwest Tropcial Stlantic Station (NTAS) observatory.","ion_geospatial_lon_min":-51,"ion_geospatial_lon_max":-51,"ion_time_coverage_start":"2011-06-20T20:00:00Z","ion_geospatial_vertical_max":0,"ion_geospatial_vertical_min":0,"title":"NTAS 10 Real-time Mooring Data, System 1","references":"http:// www.oceansites.org, http://uop.whoi.edu/projects/ntas","user_ooi_id":"Is this used?","source":"Mooring observation","ion_time_coverage_end":"2011-06-21T15:59:59Z","ion_geospatial_lat_max":15,"download_url":"http://thredds.oceanobservatories.org/thredds/dodsC/ooiciData/C5126491-7C23-4F62-A49B-BEB75B63EDEE.ncml.html","data_resource_id":"C5126491-7C23-4F62-A49B-BEB75B63EDEE","ion_geospatial_lat_min":15,"ion_geospatial_vertical_positive":"down","comment":"Argos, hourly averaged ASIMet data","institution":"WHOI"},"notificationSet":False,"date_registered":1308686613599},{"datasetMetadata":{"ion_geospatial_lon_min":-74.8399963379,"ion_geospatial_lon_max":-74.8399963379,"ion_time_coverage_start":"2011-06-20T20:50:00Z","ion_geospatial_vertical_max":-5,"ion_geospatial_vertical_min":-5,"title":"SOS (urn:ioos:station:wmo:44014) Winds","references":"http://sdf.ndbc.noaa.gov/sos/, http://example.edu/second-url-test","user_ooi_id":"Is this used?","source":"Sensor Observation Service (http://sdf.ndbc.noaa.gov/sos/server.php?)","ion_time_coverage_end":"2011-06-21T18:50:00Z","ion_geospatial_lat_max":36.6100006104,"download_url":"http://thredds.oceanobservatories.org/thredds/dodsC/ooiciData/2F73BD07-AE90-42C2-A30A-5FD83AF06A8B.ncml.html","data_resource_id":"2F73BD07-AE90-42C2-A30A-5FD83AF06A8B","ion_geospatial_lat_min":36.6100006104,"ion_geospatial_vertical_positive":"down","institution":"NOAA NDBC"},"notificationSet":False,"date_registered":1308686634113}]

DATARESOURCESUMMARY_ONE = {"title": "NDBC Sensor Observation Service data from \"http://sdf.ndbc.noaa.gov/sos/\"","data_resource_id": "3319A67F-81F3-424F-8E69-4F28C4E04802", "institution": "NOAA\'s National Data Buoy Center (http://www.ndbc.noaa.gov/)", "summary": "Real-time surface data from ASIMet system 1 on the tenth Northwest Tropcial Stlantic Station (NTAS) observatory.", "source": "NDBC SOS","ion_time_coverage_start": "2008-08-01T00:50:00Z","ion_time_coverage_end": "2008-08-01T23:50:00Z","ion_geospatial_lat_min": -45.431,"ion_geospatial_lat_max": -45.431,"ion_geospatial_lon_min": 25.909,"ion_geospatial_lon_max": 25.909,"ion_geospatial_vertical_min": 0.2,"ion_geospatial_vertical_max": 0.0,"ion_geospatial_vertical_positive": "down", "station_id":"Station 123abc", "base_url":"http://base.url.edu/testing123"
}



SUBSCRIPTION_DATA = {"subscriptionListResults": [ {"subscriptionInfo": {"user_ooi_id": "A7B44115-34BC-4553-B51E-1D87617F12E0","data_src_id": "3319A67F-81F3-424F-8E69-4F28C4E04801","subscription_type": "EMAILANDDISPATCHER","email_alerts_filter": "UPDATES","dispatcher_alerts_filter": "UPDATES","dispatcher_script_path": "path","date_registered": 1304724473336},"datasetMetadata": {"user_ooi_id": "A7B44115-34BC-4553-B51E-1D87617F12E0","data_resource_id": "3319A67F-81F3-424F-8E69-4F28C4E04801","title": "path","institution": "HYCOM","source": "HYCOM archive file","references": "","conventions": "","summary": "","comment": "","ion_time_coverage_start": "2011-04-11T00:00:00Z","ion_time_coverage_end": "2011-04-11T00:00:00Z","ion_geospatial_lat_min": 32.0284996033,"ion_geospatial_lat_max": 44.0166015625,"ion_geospatial_lon_min": -81.0400390625,"ion_geospatial_lon_max": -65.0400390625,"ion_geospatial_vertical_min": 1.0,"ion_geospatial_vertical_max": 32.0,"ion_geospatial_vertical_positive": "down","download_url": "http://localhost:8081/thredds/dodsC/scanData/3319A67F-81F3-424F-8E69-4F28C4E04801.ncml"}}, 
    {"subscriptionInfo": {"user_ooi_id": "A7B44115-34BC-4553-B51E-1D87617F1ZZZ","data_src_id": "3319A67F-81F3-424F-8E69-4F28C4E04ZZZ","subscription_type": "EMAILANDDISPATCHER","email_alerts_filter": "UPDATES","dispatcher_alerts_filter": "UPDATES","dispatcher_script_path": "path","date_registered": 1304724473336},"datasetMetadata": {"user_ooi_id": "A7B44115-34BC-4553-B51E-1D87617F12E0","data_resource_id": "3319A67F-81F3-424F-8E69-4F28C4E04ZZZ","title": "path","institution": "FOOBAR","source": "FOOBAR archive file","references": "","conventions": "","summary": "","comment": "","ion_time_coverage_start": "2011-04-11T00:00:00Z","ion_time_coverage_end": "2011-04-11T00:00:00Z","ion_geospatial_lat_min": 32.0284996033,"ion_geospatial_lat_max": 44.0166015625,"ion_geospatial_lon_min": -81.0400390625,"ion_geospatial_lon_max": -65.0400390625,"ion_geospatial_vertical_min": 1.0,"ion_geospatial_vertical_max": 32.0,"ion_geospatial_vertical_positive": "down","download_url": "http://localhost:8081/thredds/dodsC/scanData/3319A67F-81F3-424F-8E69-4F28C4E04801.ncml"}},
    {"subscriptionInfo": {"user_ooi_id": "A7B44115-34BC-4553-B51E-1D87617F1ZZZ","data_src_id": "3319A67F-81F3-424F-8E69-4F28C4E04QQQ","subscription_type": "EMAILANDDISPATCHER","email_alerts_filter": "UPDATESANDDATASOURCEOFFLINE","dispatcher_alerts_filter": "UPDATES","dispatcher_script_path": "path","date_registered": 1304724473336},"datasetMetadata": {"user_ooi_id": "A7B44115-34BC-4553-B51E-1D87617F12E0","data_resource_id": "3319A67F-81F3-424F-8E69-4F28C4E04QQQ","title": "path","institution": "BAZ","source": "BAZ archive file","references": "","conventions": "","summary": "","comment": "","ion_time_coverage_start": "2011-04-11T00:00:00Z","ion_time_coverage_end": "2011-04-11T00:00:00Z","ion_geospatial_lat_min": 32.0284996033,"ion_geospatial_lat_max": 44.0166015625,"ion_geospatial_lon_min": -81.0400390625,"ion_geospatial_lon_max": -65.0400390625,"ion_geospatial_vertical_min": 1.0,"ion_geospatial_vertical_max": 32.0,"ion_geospatial_vertical_positive": "down","download_url": "http://localhost:8081/thredds/dodsC/scanData/3319A67F-81F3-424F-8E69-4F28C4E04801.ncml"}}
]
    }


FINDBYUSER = {"datasetByOwnerMetadata": [{"data_resource_id": "3319A67F-81F3-424F-8E69-4F28C4E04802","title": "NTAS 10 Real-time Mooring Data, System 1","date_registered": 1304696743406,"ion_title": "NTAS1 Data Source","activation_state": "Public","update_interval_seconds": 60},{"data_resource_id": "3319A67F-81F3-424F-8E69-4F28C4E04805","title": "WHOTS 7 near-real-time Mooring Data, System 2","date_registered": 1304696743328,"ion_title": "WHOTS2 Data Source","activation_state": "Private","update_interval_seconds": 0},{"data_resource_id": "3319A67F-81F3-424F-8E69-4F28C4E04806","title": "7723 Moanalua RG No 1 at alt 1000 ft Oahu HI (212359157502601) - Instantaneous Value","date_registered": 1304696743377,"ion_title": "Moana Loa Data Source","activation_state": "Public","update_interval_seconds": 60},{"data_resource_id": "3319A67F-81F3-424F-8E69-4F28C4E04808","title": "CONNECTICUT RIVER AT THOMPSONVILLE CT (01184000) - Instantaneous Value","date_registered": 1304696743367,"ion_title": "Connecticut River Data Source","activation_state": "Private","update_interval_seconds": 0},{"data_resource_id": "3319A67F-81F3-424F-8E69-4F28C4E04803","title": "NTAS 10 Real-time Mooring Data, System 2","date_registered": 1304696743426,"ion_title": "NTAS2 Data Source","activation_state": "Private","update_interval_seconds": 0},{"data_resource_id": "3319A67F-81F3-424F-8E69-4F28C4E04807","title": "CHOPTANK RIVER NEAR GREENSBORO MD (01491000) - Instantaneous Value","date_registered": 1304696743397,"ion_title": "Choptank River Data Source","activation_state": "Private","update_interval_seconds": 0},{"data_resource_id": "3319A67F-81F3-424F-8E69-4F28C4E04804","title": "WHOTS 7 near-real-time Mooring Data, System 1","date_registered": 1304696743348,"ion_title": "WHOTS1 Data Source","activation_state": "Private","update_interval_seconds": 0},{"data_resource_id": "3319A67F-81F3-424F-8E69-4F28C4E04801","title": "HYCOM","date_registered": 1304696743358,"ion_title": "HyCom Data Source","activation_state": "Private","update_interval_seconds": 0}]}




