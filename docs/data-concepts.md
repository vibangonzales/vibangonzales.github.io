# 5 System Interface Design Details: Data Concepts

## 5.1 Introduction \[Informative]

This section specifies the Work Zone and Device Feed JSON Schemas.

## 5.2 WorkZoneFeed Schema

```
{
  "$id": "https://raw.githubusercontent.com/ite-org/cwz/main/schemas/1.0/WorkZoneFeed.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "CWZ v1.0 Work Zone Feed",
  "description": "The GeoJSON output of a CWZ Work Zone Feed v1.0.",
  "type": "object",
  "required": ["feed_info", "type", "features"],
```

### 5.2.1 Properties

```
    "properties": {
```

#### 5.2.1.1 feed\_info

```
    "feed_info": {
      "$ref": "https://raw.githubusercontent.com/ite-org/cwz/main/schemas/1.0/FeedInfo.json"
    },
```

#### 5.2.1.2 type

```
    "type": {
      "description": "The GeoJSON type.",
      "enum": ["FeatureCollection"]
    },
```

#### 5.2.1.3 features

```
    "features": {
      "description": "An array of GeoJSON Feature objects which represent CWZ road events.",
      "type": "array",
      "items": {
        "allOf": [
          {
            "properties": {
              "properties": {
                "properties": {
                  "core_details": {
                    "properties": {
                      "event_type": {
                        "enum": ["work-zone", "detour"]
                      }
                    },
                    "required": ["event_type"]
                  }
                },
                "required": ["core_details"]
              }
            },
            "required": ["properties"]
          },
          {
            "$ref": "https://raw.githubusercontent.com/ite-org/cwz/main/schemas/1.0/RoadEventFeature.json"
          }
        ]
      }
    },
```

#### 5.2.1.4 bbox

```
    "bbox": {
      "$ref": "https://raw.githubusercontent.com/ite-org/cwz/main/schemas/1.0/BoundingBox.json"
    }
  }
}
```

## 5.3 FeedInfo Schema

```
{
  "$id": "https://raw.githubusercontent.com/ite-org/cwz/main/schemas/1.0/FeedInfo.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "CWZ Feed Information",
  "description": "Describes CWZ feed header information such as metadata, contact information, and data sources.",
  "type": "object",
  "required": [
    "publisher",
    "update_frequency",
    "update_date",
    "version",
    "license",
    "data_sources"
  ],
```

### 5.3.1 Properties

```
    "properties": {
```

#### 5.3.1.1 publisher

```
    "publisher": {
      "description": "The organization responsible for publishing the feed.",
      "type": "string"
    },
```

#### 5.3.1.2 contact\_name

```
    "contact_name": {
      "description": "The name of the individual or group responsible for the data feed.",
      "type": "string"
    },
```

#### 5.3.1.3 contact\_email

```
    "contact_email": {
      "description": "The email address of the individual or group responsible for the data feed.",
      "type": "string",
      "format": "email"
    },
```

#### 5.3.1.4 update\_frequency

```
    "update_frequency": {
      "description": "The frequency in seconds at which the data feed is updated.",
      "type": "integer",
      "minimum": -1
    },
```

#### 5.3.1.5 update\_date

```
    "update_date": {
      "description": "The UTC date and time when the GeoJSON file (representing the instance of the feed) was generated.",
      "type": "string",
      "format": "date-time"
    },
```

#### 5.3.1.6 version

```
    "version": {
      "description": "The CWZ specification version used to create the data feed, in 'major.minor' format.",
      "type": "string",
      "pattern": "^(0|[1-9][0-9]*)\\.(0|[1-9][0-9]*)$"
    },
```

#### 5.3.1.7 license

```
    "license": {
      "description": "The URL of the license that applies to the data in the CWZ feed. This *must* be the string \"https://creativecommons.org/publicdomain/zero/1.0/\".",
      "enum": [
        "https://creativecommons.org/publicdomain/zero/1.0/"
      ]
    },
```

#### 5.3.1.8 data\_sources

```
    "data_sources": {
      "description": "A list of specific data sources for the road event data in the feed.",
      "type": "array",
      "items": {
        "$ref": "#/definitions/FeedDataSource"
      },
      "minItems": 1
    }
  },
```

### 5.3.2 Definitions

```
    "definitions": {
```

#### 5.3.2.1 FeedDataSource

```
    "FeedDataSource": {
      "title": "CWZ Feed Data Source",
      "description": "Describes information about a specific data source used to build the work zone data feed.",
      "type": "object",
      "required": [
        "data_source_id",
        "organization_name",
        "update_frequency",
        "update_date"
      ],
      "properties": {
```

##### 5.3.2.1.1 data\_source\_id

```
        "data_source_id": {
          "description": "Unique identifier for the organization providing work zone data. This identifier is a Universally Unique Identifier (UUID) as defined in [RFC 4122](https://datatracker.ietf.org/doc/html/rfc4122).",
          "type": "string"
        },
```

##### 5.3.2.1.2 organization\_name

```
        "organization_name": {
          "description": "The name of the organization for the authoritative source of the work zone data.",
          "type": "string"
        },
```

##### 5.3.2.1.3 contact\_name

```
        "contact_name": {
          "description": "The name of the individual or group responsible for the data source.",
          "type": "string"
        },
```

##### 5.3.2.1.4 contact\_email

```
        "contact_email": {
          "description": "The email address of the individual or group responsible for the data source.",
          "type": "string",
          "format": "email"
        },
```

##### 5.3.2.1.5 update\_frequency

```
        "update_frequency": {
          "description": "The frequency in seconds at which the data source is updated.",
          "type": "integer",
          "minimum": -1
        },
```

##### 5.3.2.1.6 update\_date

```
        "update_date": {
          "description": "The UTC date and time when the data source was last updated.",
          "type": "string",
          "format": "date-time"
        }
      }
    }
  }
}
```

## 5.4 RoadEventFeature Schema

```
{
  "$id": "https://raw.githubusercontent.com/ite-org/cwz/main/schemas/1.0/RoadEventFeature.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Road Event Feature (GeoJSON Feature)",
  "description": "The container object for a specific CWZ road event; an instance of a GeoJSON Feature.",
  "type": "object",
  "required": ["id","type","properties","geometry"],
```

### 5.4.1 Properties

```
    "properties": {
```

#### 5.4.1.1 id

```
    "id": {
      "description": "A unique identifier issued by the data feed provider to identify the CWZ road event. This identifier is a Universally Unique Identifier (UUID) as defined in [RFC 4122](https://datatracker.ietf.org/doc/html/rfc4122).",
      "type": "string"
    },
```

#### 5.4.1.2 type

```
    "type": {
      "description": "The GeoJSON object type; must be 'Feature'.",
      "enum": ["Feature"]
    },
```

#### 5.4.1.3 properties

```
    "properties": {
      "type": "object",
      "properties": {
        "core_details": {
          "$ref": "#/definitions/RoadEventCoreDetails"
        }
      },
      "required": ["core_details"],
      "oneOf": [
        {
          "$ref": "#/definitions/WorkZoneRoadEvent"
        },
        {
          "$ref": "#/definitions/DetourRoadEvent"
        }
      ]
    },
```

#### 5.4.1.4 geometry

```
    "geometry": {
      "oneOf": [
        {
          "$ref": "https://geojson.org/schema/LineString.json"
        },
        {
          "$ref": "https://geojson.org/schema/Point.json"
        }
      ]
    },
```

#### 5.4.1.5 bbox

```
    "bbox": {
      "$ref": "https://raw.githubusercontent.com/ite-org/cwz/main/schemas/1.0/BoundingBox.json"
    }
  },
```

### 5.4.2 Definitions

```
    "definitions": {
```

#### 5.4.2.1 WorkZoneRoadEvent

```
    "WorkZoneRoadEvent": {
      "title": "Work Zone Road Event",
      "description": "Describes a work zone road event including where, when, and what activities are taking place within a work zone on a roadway.",
      "type": "object",
      "allOf": [
        {
          "properties": {
            "core_details": {
              "properties": {
                "event_type": {
                  "const": "work-zone"
                }
              },
              "required": ["event_type"]
            }
          },
          "required": ["core_details"]
        },
        {
          "required": [
            "core_details",
            "is_start_position_verified",
            "is_end_position_verified",
            "start_date",
            "end_date",
            "is_start_date_verified",
            "is_end_date_verified",
            "vehicle_impact",
            "location_method"
          ],
          "dependencies": {
            "beginning_reference_post": ["reference_post_unit"],
            "ending_reference_post": ["reference_post_unit"]
          },
          "properties": {
```

##### 5.4.2.1.1 core\_details

```
            "core_details": {
              "$ref": "#/definitions/RoadEventCoreDetails"
            },
```

##### 5.4.2.1.2 beginning\_cross\_street

```
            "beginning_cross_street": {
              "description": "Name or number of the nearest cross street along the roadway where the event begins.",
              "type": "string"
            },
```

##### 5.4.2.1.3 ending\_cross\_street

```
            "ending_cross_street": {
              "description": "Name or number of the nearest cross street along the roadway where the event ends.",
              "type": "string"
            },
```

##### 5.4.2.1.4 beginning\_reference\_post

```
            "beginning_reference_post": {
              "description": "The linear distance measured against a reference post marker along a roadway where the event begins.",
              "type": "number",
              "minimum": 0
            },
```

##### 5.4.2.1.5 ending\_reference\_post

```
            "ending_reference_post": {
              "description": "The linear distance measured against a reference post marker along a roadway where the event ends.",
              "type": "number",
              "minimum": 0
            },
```

##### 5.4.2.1.6 reference\_post\_unit

```
            "reference_post_unit ": {
              "description": "The unit used for reference post.",
              "$ref": "#/definitions/UnitOfMeasurement"
            },
```

##### 5.4.2.1.7 is\_start\_position\_verified

```
            "is_start_position_verified": {
              "description": "Indicates if the start position (first geometric coordinate pair) is based on actual reported data from a GPS-equipped device that measured the location of the start of the work zone.",
              "type": "boolean"
            },
```

##### 5.4.2.1.8 is\_end\_position\_verified

```
            "is_end_position_verified": {
              "description": "Indicates if the end position (last geometric coordinate pair) is based on actual reported data from a GPS-equipped device that measured the location of the end of the work zone.",
              "type": "boolean"
            },
```

##### 5.4.2.1.9 start\_date

```
            "start_date": {
              "description": "The UTC date and time (formatted according to RFC 3339, Section 5.6) when the road event begins (e.g., 2020-11-03T19:37:00Z).",
              "type": "string",
              "format": "date-time"
            },
```

##### 5.4.2.1.10 end\_date

```
            "end_date": {
              "description": "The UTC date and time (formatted according to RFC 3339, Section 5.6) when the road event ends (e.g., 2020-11-03T19:37:00Z).",
              "type": "string",
              "format": "date-time"
            },
```

##### 5.4.2.1.11 is\_start\_date\_verified

```
            "is_start_date_verified": {
              "description": "Indicates if work has been confirmed to have started, such as from a person or field device.",
              "type": "boolean"
            },
```

##### 5.4.2.1.12 is\_end\_date\_verified

```
            "is_end_date_verified": {
              "description": "Indicates if work has been confirmed to have ended, such as from a person or field device.",
              "type": "boolean"
            },
```

##### 5.4.2.1.13 work\_zone\_type

```
            "work_zone_type": {
              "description": "The type of work zone road event.",
              "$ref": "#/definitions/WorkZoneType"
            },
```

##### 5.4.2.1.14 vehicle\_impact

```
            "vehicle_impact": {
              "$ref": "#/definitions/VehicleImpact"
            },
```

##### 5.4.2.1.15 location\_method

```
            "location_method": {
              "$ref": "#/definitions/LocationMethod"
            },
```

##### 5.4.2.1.16 worker\_presence

```
            "worker_presence": {
              "$ref": "#/definitions/WorkerPresence"
            },
```

##### 5.4.2.1.17 reduced\_speed\_limit\_kph

```
            "reduced_speed_limit_kph": {
              "description": "If applicable, the reduced speed limit posted within the road event, in kilometers per hour.",
              "type": "number",
              "minimum": 0
            },
```

##### 5.4.2.1.18 restrictions

```
            "restrictions": {
              "description": "A list of zero or more restrictions applying to the road event.",
              "type": "array",
              "items": {
                "$ref": "#/definitions/Restriction"
              }
            },
```

##### 5.4.2.1.19 types\_of\_work

```
            "types_of_work": {
              "description": "A list of the types of work being done in a road event.",
              "type": "array",
              "items": {
                "$ref": "#/definitions/TypeOfWork"
              }
            },
```

##### 5.4.2.1.20 lanes

```
            "lanes": {
              "description": "A list of individual lanes within a road event (roadway segment).",
              "type": "array",
              "items": {
                "$ref": "#/definitions/Lane"
              }
            },
```

##### 5.4.2.1.21 impacted\_cds\_curb\_zones

```
            "impacted_cds_curb_zones": {
               "description": "A list of references to external CDS Curb Zones impacted by the work zone.",
               "type": "array",
               "items": {
                  "$ref": "#/definitions/CdsCurbZonesReference"
              }
            }
          }
        }
      ]
    },
```

#### 5.4.2.2 DetourRoadEvent

```
    "DetourRoadEvent": {
      "title": "Detour Road Event",
      "description": "Describes a detour on a roadway.",
      "type": "object",
      "allOf": [
        {
          "properties": {
            "core_details": {
              "properties": {
                "event_type": {
                  "const": "detour"
                }
              },
              "required": ["event_type"]
            }
          },
          "required": ["core_details"]
        },
        {
          "required": [
            "core_details",
            "start_date",
            "end_date",
            "is_start_date_verified",
            "is_end_date_verified"
          ],
          "dependencies": {
            "beginning_reference_post": ["reference_post_unit"],
            "ending_reference_post": ["reference_post_unit"]
          },
          "properties": {
```

##### 5.4.2.2.1 core\_details

```
            "core_details": {
              "$ref": "#/definitions/RoadEventCoreDetails"
            },
```

##### 5.4.2.2.2 beginning\_cross\_street

```
            "beginning_cross_street": {
              "description": "Name or number of the nearest cross street along the roadway where the event begins.",
              "type": "string"
            },
```

##### 5.4.2.2.3 ending\_cross\_street

```
            "ending_cross_street": {
              "description": "Name or number of the nearest cross street along the roadway where the event ends.",
              "type": "string"
            },
```

##### 5.4.2.2.4 beginning\_reference\_post

```
            "beginning_reference_post": {
              "description": "The linear distance measured against a reference post marker along a roadway where the event begins.",
              "type": "number",
              "minimum": 0
            },
```

##### 5.4.2.2.5 ending\_reference\_post

```
            "ending_reference_post": {
              "description": "The linear distance measured against a reference post marker along a roadway where the event ends.",
              "type": "number",
              "minimum": 0
            },
```

##### 5.4.2.2.6 reference\_post\_unit

```
            "reference_post_unit": {
              "description": "The unit used for reference post.",
              "$ref": "#/definitions/UnitOfMeasurement"
            },
```

##### 5.4.2.2.7 start\_date

```
            "start_date": {
              "description": "The UTC date and time (formatted according to RFC 3339, Section 5.6) when the road event begins (e.g., 2020-11-03T19:37:00Z).",
              "type": "string",
              "format": "date-time"
            },
```

##### 5.4.2.2.8 end\_date

```
            "end_date": {
              "description": "The UTC date and time (formatted according to RFC 3339, Section 5.6) when the road event ends (e.g., 2020-11-03T19:37:00Z).",
              "type": "string",
              "format": "date-time"
            },
```

##### 5.4.2.2.9 is\_start\_date\_verified

```
            "is_start_date_verified": {
              "description": "Indicates if the detour has been confirmed to have started, such as from a person or device in the field or a report from a traffic management center.",
              "type": "boolean"
            },
```

##### 5.4.2.2.10 is\_end\_date\_verified

```
            "is_end_date_verified": {
              "description": "Indicates if the detour has been confirmed to have ended, such as from a person or device in the field or a report from a traffic management center.",
              "type": "boolean"
            }
          }
        }
      ]
    },
```

#### 5.4.2.3 RoadEventCoreDetails

```
    "RoadEventCoreDetails": {
      "title": "Road Event Core Details",
      "description": "The core details of an event occurring on a roadway (i.e. a road event) that is shared by all types of road events.",
      "type": "object",
      "required": [
        "data_source_id",
        "event_type",
        "road_names",
        "direction"
      ],
      "properties": {
```

##### 5.4.2.3.1 data\_source\_id

```
        "data_source_id": {
          "description": "Identifies the data source from which the road event data is sourced from.",
          "type": "string"
        },
```

##### 5.4.2.3.2 event\_type

```
        "event_type": {
          "$ref": "#/definitions/EventType"
        },
```

##### 5.4.2.3.3 related\_road\_events

```
        "related_road_events": {
          "description": "A list describing one or more road events which are related to this road event, such as a work zone project it is part of or another road event that occurs before or after it in sequence.",
          "type": "array",
          "items": {
            "$ref": "#/definitions/RelatedRoadEvent"
          }
        },
```

##### 5.4.2.3.4 project\_id

```
        "project_id": {
          "description": " An identifier for the project that the event is part of. A project is the highest-level representation of an area where road work takes place and may cover multiple roadways if adjacent or intersecting. A project will contain one or more RoadEventFeatures. This project ID does not correspond to an object in a WorkZoneFeed. It is used to group events (and devices, see FieldDeviceCoreDetails). This identifier is a Universally Unique Identifier (UUID) as defined in RFC 4122 to guarantee uniqueness between feeds and over time.",
          "type": "string"
        },
```

##### 5.4.2.3.5 road\_names

```
        "road_names": {
          "description": "A list of publicly known names of the road on which the event occurs. This may include the road number designated by a jurisdiction such as a county, state or interstate (e.g., I-5, VT 133).",
          "type": "array",
          "minItems": 1,
          "items": {
            "type": "string"
          }
        },
```

##### 5.4.2.3.6 direction

```
        "direction": {
          "$ref": "https://raw.githubusercontent.com/ite-org/cwz/main/schemas/1.0/Direction.json"
        },
```

##### 5.4.2.3.7 name

```
        "name": {
          "description": "A human-readable name for the road event.",
          "type": "string"
        },
```

##### 5.4.2.3.8 description

```
        "description": {
          "description": "Short free text description of the road event.",
          "type": "string"
        },
```

##### 5.4.2.3.9 creation\_date

```
        "creation_date": {
          "description": "The UTC date and time (formatted according to RFC 3339, Section 5.6) when the road event was created (e.g., 2020-11-03T19:37:00Z).",
          "type": "string",
          "format": "date-time"
        },
```

##### 5.4.2.3.10 update\_date

```
        "update_date": {
          "description": "The UTC date and time (formatted according to RFC 3339, Section 5.6) when any information in the RoadEventFeature (including child objects) that the RoadEventCoreDetails applies to was most recently updated or confirmed as up to date.",
          "type": "string",
          "format": "date-time"
        }
      }
    },
```

#### 5.4.2.4 LocationMethod

```
    "LocationMethod": {
      "title": "Location Method Enumerated Type",
      "description": "The typical method used to locate the beginning and end of a work zone impact area.",
      "enum": [
        "channel-device-method",
        "sign-method",
        "junction-method",
        "other",
        "unknown"
      ]
    },
```

#### 5.4.2.5 RelatedRoadEvent

```
    "RelatedRoadEvent": {
      "title": "RelatedRoadEvent",
      "description": "Identifies a road event that is related to the road event that the RelatedRoadEvent object occurs on.",
      "type": "object",
      "required": ["type", "id"],
      "properties": {
```

##### 5.4.2.5.1 type

```
        "type": {
          "description": "The type of road event being identified, such as another sequence of related work zones, a detour, or next road event in sequence.",
          "$ref": "#/definitions/RelatedRoadEventType"
        },
```

##### 5.4.2.5.2 id

```
        "id": {
          "description": "An identifier for the related road event by the type property.",
          "type": "string"
        }
      }
    },
```

#### 5.4.2.6 TypeOfWork

```
    "TypeOfWork": {
      "title": "Type of Work",
      "description": "A description of the type of work being done in a road event and an indication of if that work will result in an architectural change to the roadway.",
      "type": "object",
      "required": ["type_name"],
      "properties": {
```

##### 5.4.2.6.1 type\_name

```
        "type_name": {
          "$ref": "#/definitions/WorkTypeName"
        },
```

##### 5.4.2.6.2 is\_architectural\_change

```
        "is_architectural_change": {
          "description": "A flag indicating whether the type of work will result in an architectural change to the roadway.",
          "type": "boolean"
        }
      }
    },
```

#### 5.4.2.7 Lane

```
    "Lane": {
      "title": "Lane",
      "description": "An individual lane within a road event.",
      "type": "object",
      "required": ["order", "status", "type"],
      "properties": {
```

##### 5.4.2.7.1 order

```
        "order": {
          "description": "The position (index) of the lane in sequence on the roadway, where '1' represents the left-most lane.",
          "type": "integer",
          "minimum": 1
        },
```

##### 5.4.2.7.2 status

```
        "status": {
          "$ref": "#/definitions/LaneStatus"
        },
```

##### 5.4.2.7.3 type

```
        "type": {
          "$ref": "#/definitions/LaneType"
        },
```

##### 5.4.2.7.4 restrictions

```
        "restrictions": {
          "description": "A list of zero or more restrictions specific to the lane.",
          "type": "array",
          "items": {
            "$ref": "#/definitions/Restriction"
          }
        }
      }
    },
```

#### 5.4.2.8 Restriction

```
    "Restriction": {
      "title": "Restriction",
      "description": "A restriction on a roadway or lane, including type and value.",
      "type": "object",
      "required": ["type"],
      "dependencies": {
        "value": ["unit"]
      },
      "properties": {
```

##### 5.4.2.8.1 type

```
        "type": {
          "$ref": "#/definitions/RestrictionType"
        },
```

##### 5.4.2.8.2 value

```
        "value": {
          "type": "number"
        },
```

##### 5.4.2.8.3 unit

```
        "unit": {
          "$ref": "#/definitions/UnitOfMeasurement"
        }
      }
    },
```

#### 5.4.2.9 CdsCurbZonesReference

```
    "CdsCurbZonesReference": {
      "title": "CdsCurbZonesReference",
      "description": "A reference to one or more CDS curb zones that are impacted by road work.",
      "type": "object",
      "required": ["cds_curb_zone_ids", "cds_curbs_api_url"],
      "properties": {
```

##### 5.4.2.9.1 cds\_curb\_zone\_ids

```
          "cds_curb_zone_ids": {
             "description": "A list of CDS Curb Zone ids.",
             "type": "array",
             "items": {
                "type": "string"
             }
          },
```

##### 5.4.2.9.2 cds\_curbs\_api\_url

```
          "cds_curbs_api_url": {
            "description": "An identifier for the source of the requested CDS Curbs API.",
            "type": "string",
            "format": "uri"
          }
      }
  },
```

#### 5.4.2.10 WorkerPresence

```
    "WorkerPresence": {
      "title": "Worker Presence",
      "description": "Information about the presence of workers in the work zone event area.",
      "type": "object",
      "required": ["are_workers_present"],
      "properties": {
```

##### 5.4.2.10.1 are\_workers\_present

```
        "are_workers_present": {
          "description": "Whether workers are present in the work zone event area, following the definition provided in the 'definition' property on the WorkerPresence object.",
          "type": "boolean"
        },
```

##### 5.4.2.10.2 method

```
        "method": {
          "$ref": "#/definitions/WorkerPresenceMethod"
        },
```

##### 5.4.2.10.3 worker\_presence\_last\_confirmed\_date

```
        "worker_presence_last_confirmed_date": {
          "description": "The UTC date and time at which the presence of workers was last confirmed.",
          "type": "string",
          "format": "date-time"
        },
```

##### 5.4.2.10.4 confidence

```
        "confidence": {
          "$ref": "#/definitions/WorkerPresenceConfidence"
        },
```

##### 5.4.2.10.5 definition

```
        "definition": {
          "description": "A list of situations in which workers are considered to be present in the jurisdiction of the data provider.",
          "type": "array",
          "items": {
            "$ref": "#/definitions/WorkerPresenceDefinition"
          },
          "uniqueItems": true
        },
```

##### 5.4.2.10.6 other\_method

```
        "other_method": {
          "description": "Provides more information about how worker presence in a work zone event area is determined when method enumeration selected is 'other'.",
          "type": "string"
        }
      }
    },
```

#### 5.4.2.11 EventType

```
    "EventType": {
      "title": "Road Event Type Enumerated Type",
      "description": "The type of CWZ road event.",
      "enum": ["work-zone", "detour"]
    },
```

#### 5.4.2.12 WorkZoneType

```
    "WorkZoneType": {
      "title": "Work Zone Type Enumerated Type",
      "description": "The type of work zone road event.",
      "enum": ["static", "moving", "planned-moving-area"]
    },
```

#### 5.4.2.13 VehicleImpact

```
    "VehicleImpact": {
      "title": "Vehicle Impact Enumerated Type",
      "description": "The impact to vehicular lanes along a single road in a single direction.",
      "enum": ["all-lanes-closed", "some-lanes-closed", "all-lanes-open", "alternating-one-way", "some-lanes-closed-merge-left", "some-lanes-closed-merge-right", "all-lanes-open-shift-left", "all-lanes-open-shift-right", "some-lanes-closed-split", "flagging", "temporary-traffic-signal", "unknown"]
    },
```

#### 5.4.2.14 RestrictionType

```
    "RestrictionType": {
      "title": "Restriction Type Enumerated Type",
      "description": "The type of vehicle restriction on a roadway.",
      "enum": [
        "local-access-only",
        "no-trucks",
        "travel-peak-hours-only",
        "hov-3",
        "hov-2",
        "no-parking",
        "reduced-width",
        "reduced-height",
        "reduced-length",
        "reduced-weight",
        "axle-load-limit",
        "gross-weight-limit",
        "towing-prohibited",
        "permitted-oversize-loads-prohibited",
        "no-passing"
      ]
    },
```

#### 5.4.2.15 WorkTypeName

```
    "WorkTypeName": {
      "title": "Work Type Name Enumerated Type",
      "description": "A high-level text description of the type of work being done in a road event.",
      "enum": [
        "non-encroachment",
        "minor-road-defect-repair",
        "roadside-work",
        "overhead-work",
        "below-road-work",
        "barrier-work",
        "surface-work",
        "painting",
        "roadway-relocation",
        "roadway-creation"
      ]
    },
```

#### 5.4.2.16 LaneStatus

```
    "LaneStatus": {
      "title": "Lane Status Enumerated Type",
      "description": "The status of the lane for the traveling public.",
      "enum": ["open", "closed", "shift-left", "shift-right", "merge-left", "merge-right", "alternating-flow"]
    },
```

#### 5.4.2.17 LaneType

```
    "LaneType": {
      "title": "Lane Type Enumerated Type",
      "description": "An indication of the type of lane or shoulder.",
      "enum": [
        "general",
        "exit-lane",
        "exit-ramp",
        "entrance-lane",
        "entrance-ramp",
        "sidewalk",
        "bike-lane",
        "shoulder",
        "parking",
        "median",
        "two-way-center-turn-lane"
      ]
    },
```

#### 5.4.2.18 UnitOfMeasurement

```
    "UnitOfMeasurement": {
      "title": "Unit of Measurement Enumerated Type",
      "description": "Unit of measurement, used when providing a unit to accompany a value.",
      "enum": ["feet", "inches", "centimeters", "pounds", "tons", "kilograms", "miles", "kilometers"]
    },
```

#### 5.4.2.19 WorkerPresenceMethod

```
    "WorkerPresenceMethod": {
      "title": "Worker Presence Method Enumerated Type",
      "description": "Describes methods for how worker presence in a work zone event area is determined.",
      "enum": [
        "camera-monitoring",
        "maintenance-vehicle-present",
        "wearables-present",
        "mobile-device-present",
        "check-in-app",
        "check-in-verbal",
        "other"
      ]
    },
```

#### 5.4.2.20 WorkerPresenceDefinition

```
    "WorkerPresenceDefinition": {
      "title": "Worker Presence Definition Enumerated Type",
      "description": "Situations in which workers may be considered present in a work zone.",
      "enum": [
        "workers-in-work-zone-working",
        "workers-in-work-zone-not-working",
        "mobile-equipment-in-work-zone-moving",
        "mobile-equipment-in-work-zone-not-moving",
        "fixed-equipment-in-work-zone",
        "humans-behind-barrier",
        "humans-in-right-of-way"
      ]
    },
```

#### 5.4.2.21 WorkerPresenceConfidence

```
    "WorkerPresenceConfidence": {
      "title": "Worker Presence Confidence Enumerated Type",
      "description": "A high-level description of the feed publisher's confidence in the reported WorkerPresence value of are_workers_present.",
      "enum": [
        "low",
        "medium",
        "high"
      ]
    },
```

#### 5.4.2.22 RelatedRoadEventType

```
    "RelatedRoadEventType": {
      "title": "Related Road Event Type Enumerated Type",
      "description": "Describes how a road event is related to the road event that the RelatedRoadEvent object occurs on.",
      "enum": [
        "first-in-sequence",
        "next-in-sequence",
        "first-occurrence",
        "next-occurrence",
        "related-work-zone",
        "related-detour",
        "planned-moving-operation",
        "active-moving-operation"
      ]
    }
  }
}
```

## 5.5 DeviceFeed Schema

```
{
  "$id": "https://raw.githubusercontent.com/ite-org/cwz/main/schemas/1.0/DeviceFeed.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "CWZ v1.0 DeviceFeed",
  "description": "The GeoJSON output of a CWZ Device Feed v1.0.",
  "type": "object",
  "required": ["feed_info", "type", "features"],
```

### 5.5.1 Properties

```
    "properties": {
```

#### 5.5.1.1 feed\_info

```
    "feed_info": {
      "$ref": "https://raw.githubusercontent.com/ite-org/cwz/main/schemas/1.0/FeedInfo.json"
    },
```

#### 5.5.1.2 type

```
    "type": {
      "description": "The GeoJSON type.",
      "enum": ["FeatureCollection"]
    },
```

#### 5.5.1.3 features

```
    "features": {
      "description": "An array of GeoJSON Feature objects which represent field devices deployed in a work zone.",
      "type": "array",
      "items": {
        "$ref": "#/definitions/FieldDeviceFeature"
      }
    },
```

#### 5.5.1.4 bbox

```
    "bbox": {
      "$ref": "https://raw.githubusercontent.com/ite-org/cwz/main/schemas/1.0/BoundingBox.json"
    }
  },
```

### 5.5.2 Definitions

```
    "definitions": {
```

#### 5.5.2.1 FieldDeviceFeature

```
    "FieldDeviceFeature": {
      "title": "Field Device Feature (GeoJSON Feature)",
      "description": "The GeoJSON feature container for a CWZ field device.",
      "type": "object",
 "required": ["id","type","properties","geometry"],
      "properties": {
```

##### 5.5.2.1.1 id

```
        "id": {
          "description": "A unique identifier issued by the data feed provider to identify the field device. This identifier is a Universally Unique Identifier (UUID) as defined in [RFC 4122](https://datatracker.ietf.org/doc/html/rfc4122).",
          "type": "string"
        },
```

##### 5.5.2.1.2 type

```
        "type": {
          "description": "The GeoJSON object type; must be 'Feature'.",
          "enum": ["Feature"]
        },
```

##### 5.5.2.1.3 properties

```
        "properties": {
          "type": "object",
          "properties": {
            "core_details": {
              "$ref": "#/definitions/FieldDeviceCoreDetails"
            }
          },
          "required": ["core_details"],
          "oneOf": [
            {
              "$ref": "#/definitions/ArrowBoard"
            },
            {
              "$ref": "#/definitions/Camera"
            },
            {
              "$ref": "#/definitions/DynamicMessageSign"
            },
            {
              "$ref": "#/definitions/FlashingBeacon"
            },
            {
              "$ref": "#/definitions/HybridSign"
            },
            {
              "$ref": "#/definitions/LocationMarker"
            },
            {
              "$ref": "#/definitions/RoadsideUnit"
            },
            {
              "$ref": "#/definitions/TrafficSensor"
            },
            {
              "$ref": "#/definitions/TrafficSignal"
            }
          ]
        },
```

##### 5.5.2.1.4 geometry

```
        "geometry": {
          "oneOf": [
            {
              "$ref": "https://geojson.org/schema/Point.json"
            }
          ]
        },
```

##### 5.5.2.1.5 bbox

```
        "bbox": {
          "$ref": "https://raw.githubusercontent.com/ite-org/cwz/main/schemas/1.0/BoundingBox.json"
        }
      }
    },
```

#### 5.5.2.2 FieldDeviceCoreDetails

```
    "FieldDeviceCoreDetails": {
      "title": "Field Device Core Details",
      "description": "The core details—both configuration and current state—of a field device that are shared by all types of field devices.",
      "type": "object",
 "required": [
        "device_type",
        "data_source_id",
        "device_status",
        "update_date",
        "has_automatic_location"
      ],
      "dependencies": {
        "reference_post": ["reference_post_unit"]
      },
      "properties": {
```

##### 5.5.2.2.1 device\_type

```
        "device_type": {
          "$ref": "#/definitions/FieldDeviceType"
        },
```

##### 5.5.2.2.2 data\_source\_id

```
        "data_source_id": {
          "description": "Identifies the data source from which the field device information is sourced from.",
          "type": "string"
        },
```

##### 5.5.2.2.3 device\_status

```
        "device_status": {
          "$ref": "#/definitions/FieldDeviceStatus"
        },
```

##### 5.5.2.2.4 update\_date

```
        "update_date": {
          "description": "The UTC date and time (formatted according to RFC 3339, Section 5.6) when any information in the FieldDeviceFeature (including child objects) that the FieldDeviceCoreDetails applies to was most recently updated or confirmed as up to date.",
          "type": "string",
          "format": "date-time"
        },
```

##### 5.5.2.2.5 has\_automatic\_location

```
        "has_automatic_location": {
          "description": "A yes/no value indicating if the field device location (parent FieldDeviceFeature's geometry) is determined automatically from an onboard GPS (true) or manually set/overridden (false).",
          "type": "boolean"
        },
```

##### 5.5.2.2.6 road\_direction

```
        "road_direction": {
          "$ref": "https://raw.githubusercontent.com/ite-org/cwz/main/schemas/1.0/Direction.json",
          "description": "The direction of the road that the field device is on. This value indicates the direction of the traffic flow of the road, not a real heading angle."
        },
```

##### 5.5.2.2.7 road\_names

```
        "road_names": {
          "description": "A list of publicly known names of the road on which the field device is located. This may include the road number designated by a jurisdiction such as a county, state or interstate (e.g., I-5, VT 133).",
          "type": "array",
          "minItems": 1,
          "items": {
            "type": "string"
          }
        },
```

##### 5.5.2.2.8 name

```
        "name": {
          "type": "string",
          "description": "A human-readable name for the field device."
        },
```

##### 5.5.2.2.9 description

```
        "description": {
          "type": "string",
          "description": "A description of the field device."
        },
```

##### 5.5.2.2.10 status\_messages

```
        "status_messages": {
          "type": "array",
          "description": "A list of messages associated with the device's status, if applicable. Used to provide additional information about the status such as specific warning or error message.",
          "items": {
            "type": "string"
          }
        },
```

##### 5.5.2.2.11 is\_moving

```
        "is_moving": {
          "type": "boolean",
          "description": "A yes/no value indicating if the device is actively moving (not statically placed) as part of a mobile work zone operation."
        },
```

##### 5.5.2.2.12 road\_event\_ids

```
        "road_event_ids": {
          "type": "array",
          "description": "A list of one or more IDs of a RoadEventFeatures that the device is associated with.",
          "items": {
            "type": "string"
          }
        },
```

##### 5.5.2.2.13 project\_id

```
        "project_id": {
          "type": "string",
          "description": " An identifier for the project that the device is associated with. A project is the highest-level representation of an area where road work takes place and may cover multiple roadways if adjacent or intersection. This project ID does not correspond to an object in a WorkZoneFeed. It is used to group devices (and events, see RoadEventCoreDetails)."
        },
```

##### 5.5.2.2.14 reference\_post

```
        "reference_post": {
          "type": "number",
          "description": "The linear distance measured against a reference post marker along a roadway where the device is located."
        },
```

##### 5.5.2.2.15 reference\_post\_unit

```
        "reference_post_unit": {
          "description": "The unit used for reference post.",
          "$ref": "#/definitions/UnitOfMeasurement"
        },
```

##### 5.5.2.2.16 make

```
        "make": {
          "type": "string",
          "description": "The make or manufacturer of the device."
        },
```

##### 5.5.2.2.17 model

```
        "model": {
          "type": "string",
          "description": "The model of the device."
        },
```

##### 5.5.2.2.18 serial\_number

```
        "serial_number": {
          "type": "string",
          "description": "The serial number of the device."
        },
```

##### 5.5.2.2.19 firmware\_version

```
        "firmware_version": {
          "type": "string",
          "description": "The version of firmware the device is using to operate."
        },
```

##### 5.5.2.2.20 velocity\_kph

```
        "velocity_kph": {
          "type": "number",
          "description": "The velocity of the device in kilometers per hour."
        },
```

##### 5.5.2.2.21 is\_in\_transport\_position

```
        "is_in_transport_position": {
          "type": "boolean",
          "description": "A yes/no value indicating if the device is in the stowed/transport position (true) or deployed/upright position (false)."
        }
      }
    },
```

<h1 style="color: red;">Left off here</h1>

#### 5.5.2.3 ArrowBoard

```
    "ArrowBoard": {
      "title": "Arrow Board Field Device",
      "description": "An electronic, connected arrow board which can display an arrow pattern to direct traffic.",
      "type": "object",
      "allOf": [
        {
          "properties": {
            "core_details": {
              "properties": {
                "device_type": {
                  "const": "arrow-board"
                }
              },
              "required": ["device_type"]
            }
          },
          "required": ["core_details"]
        },
        {
          "required": [
            "core_details",
            "pattern"
          ],
          "properties": {
```

##### 5.5.2.3.1 core\_details

```
            "core_details": {
              "$ref": "#/definitions/FieldDeviceCoreDetails"
            },
```

##### 5.5.2.3.2 pattern

```
            "pattern": {
              "$ref": "#/definitions/ArrowBoardPattern"
            }
          }
        }
      ]
    },
```

#### 5.5.2.4 Camera

```
    "Camera": {
      "title": "Camera Field Device",
      "description": "A camera device deployed in the field, capable of capturing still images.",
      "type": "object",
      "allOf": [
        {
          "properties": {
            "core_details": {
              "properties": {
                "device_type": {
                  "const": "camera"
                }
              },
              "required": ["device_type"]
            }
          },
          "required": ["core_details"]
        },
        {
          "required": [
            "core_details"
          ],
          "dependencies": {
            "image_url": ["image_timestamp"],
            "video_url": ["video_update_frequency"]
          },
          "properties": {
```

##### 5.5.2.4.1 core\_details

```
            "core_details": {
              "$ref": "#/definitions/FieldDeviceCoreDetails"
            },
```

##### 5.5.2.4.2 image\_url

```
            "image_url": {
              "type": "string",
              "format": "uri",
              "description": "A URL pointing to an image file for the camera video."
            },
```

##### 5.5.2.4.3 is\_image\_url\_public

```
            "is_image_url_public": {
              "type": "boolean",
              "description": "Identifies whether image_url is publicly accessible."
            },
```

##### 5.5.2.4.4 image\_timestamp

```
            "image_timestamp": {
              "type": "string",
              "format": "date-time",
              "description": "The UTC date and time when the image was captured."
            },
```

##### 5.5.2.4.5 video\_url

```
            "video_url": {
              "type": "string",
              "format": "uri",
              "description": "A URL pointing to a video file for the camera video."
            },
```

##### 5.5.2.4.6 is\_video\_url\_public

```
            "is_video_url_public": {
              "type": "boolean",
              "description": "Identifies whether video_url is publicly accessible."
            },
```

##### 5.5.2.4.7 video\_update\_frequency

```
            "video_update_frequency": {
              "description": "The frequency at which the video feed is updated, in seconds.",
              "type": "integer",
              "minimum": -1
            }
          }
        }
      ]
    },
```

#### 5.5.2.5 DynamicMessageSign

```
    "DynamicMessageSign": {
      "title": "Dynamic Message Sign Field Device",
      "description": "An electronic traffic sign deployed on the roadway, used to provide information to travelers.",
      "allOf": [
        {
          "properties": {
            "core_details": {
              "properties": {
                "device_type": {
                  "const": "dynamic-message-sign"
                }
              },
              "required": ["device_type"]
            }
          },
          "required": ["core_details"]
        },
        {
          "required": [
            "core_details",
            "message_multi_string"
          ],
          "properties": {
```

##### 5.5.2.5.1 core\_details

```
            "core_details": {
              "$ref": "#/definitions/FieldDeviceCoreDetails"
            },
```

##### 5.5.2.5.2 message\_multi\_string

```
            "message_multi_string": {
              "type": "string",
              "description": "A MULTI-formatted string describing the message currently posted to the sign."
            }
          }
        }
      ]
    },
```

#### 5.5.2.6 FlashingBeacon

```
    "FlashingBeacon": {
      "title": "Flashing Beacon Field Device",
      "description": "A flashing warning beacon used to supplement a temporary traffic control device.",
      "allOf": [
        {
          "properties": {
            "core_details": {
              "properties": {
                "device_type": {
                  "const": "flashing-beacon"
                }
              },
              "required": ["device_type"]
            }
          },
          "required": ["core_details"]
        },
        {
          "required": [
            "core_details",
            "function"
          ],
          "properties": {
```

##### 5.5.2.6.1 core\_details

```
            "core_details": {
              "$ref": "#/definitions/FieldDeviceCoreDetails"
            },
```

##### 5.5.2.6.2 function

```
            "function": {
              "$ref": "#/definitions/FlashingBeaconFunction"
            },
```

##### 5.5.2.6.3 is\_flashing

```
            "is_flashing": {
              "type": "boolean",
              "description": "A yes/no value indicating if the flashing beacon is currently in use and flashing."
            },
```

##### 5.5.2.6.4 sign\_text

```
            "sign_text": {
              "type": "string",
              "description": "The text on the sign the beacon is mounted on, if applicable."
            }
          }
        }
      ]
    },
```

#### 5.5.2.7 HybridSign

```
    "HybridSign": {
      "title": "Hybrid Sign Field Device",
      "description": "A hybrid sign that contains static text (e.g., on an aluminum sign) along with a single electronic message display, used to provide information to travelers.",
      "type": "object",
      "allOf": [
        {
          "properties": {
            "core_details": {
              "properties": {
                "device_type": {
                  "const": "hybrid-sign"
                }
              },
              "required": ["device_type"]
            }
          },
          "required": ["core_details"]
        },
        {
          "required": [
            "core_details",
            "dynamic_message_function"
          ],
          "properties": {
```

##### 5.5.2.7.1 core\_details

```
            "core_details": {
              "$ref": "#/definitions/FieldDeviceCoreDetails"
            },
```

##### 5.5.2.7.2 dynamic\_message\_function

```
            "dynamic_message_function": {
              "$ref": "#/definitions/HybridSignDynamicMessageFunction"
            },
```

##### 5.5.2.7.3 dynamic\_message\_text

```
            "dynamic_message_text": {
              "type": "string",
              "description": "A text representation of the message currently posted to the dynamic electronic component of the hybrid sign."
            },
```

##### 5.5.2.7.4 static\_sign\_text

```
            "static_sign_text": {
              "type": "string",
              "description": "The static text on the non-electronic component of the hybrid sign."
            }
          }
        }
      ]
    },
```

#### 5.5.2.8 LocationMarker

```
    "LocationMarker": {
      "title": "Location Marker Field Device",
      "description": "Any GPS-enabled ITS device that is placed at a point on a roadway to dynamically know the location of something (often the beginning or end of a work zone).",
      "type": "object",
      "allOf": [
        {
          "properties": {
            "core_details": {
              "properties": {
                "device_type": {
                  "const": "location-marker"
                }
              },
              "required": ["device_type"]
            }
          },
          "required": ["core_details"]
        },
        {
          "required": ["core_details", "marked_locations"],
          "properties": {
```

##### 5.5.2.8.1 core\_details

```
            "core_details": {
              "$ref": "#/definitions/FieldDeviceCoreDetails"
            },
```

##### 5.5.2.8.2 marked\_locations

```
            "marked_locations": {
              "type": "array",
              "minItems": 1,
              "items": {
                "$ref": "#/definitions/MarkedLocation"
              }
            }
          }
        }
      ]
    },
```

#### 5.5.2.9 MarkedLocation

```
    "MarkedLocation": {
      "title": "Marked Location",
      "description": "Describes a specific location where a LocationMarker is placed, such as the start or end of a work zone road event.",
      "required": ["type"],
      "properties": {
```

##### 5.5.2.9.1 type

```
        "type": {
          "$ref": "#/definitions/MarkedLocationType"
        },
```

##### 5.5.2.9.2 road\_event\_id

```
        "road_event_id": {
          "type": "string",
          "description": "The ID of a RoadEventFeature that the MarkedLocation applies to."
        }
      }
    },
```

#### 5.5.2.10 TrafficSensor

```
    "TrafficSensor": {
      "title": "Traffic Sensor Field Device",
      "description": "A traffic sensor deployed on a roadway which captures traffic metrics (e.g., speed, volume, occupancy) over a collection interval.",
      "type": "object",
      "allOf": [
        {
          "properties": {
            "core_details": {
              "properties": {
                "device_type": {
                  "const": "traffic-sensor"
                }
              },
              "required": ["device_type"]
            }
          },
          "required": ["core_details"]
        },
        {
          "required": [
            "core_details",
            "collection_interval_start_date",
            "collection_interval_end_date"
          ],
          "properties": {
```

##### 5.5.2.10.1 core\_details

```
            "core_details": {
              "$ref": "#/definitions/FieldDeviceCoreDetails"
            },
```

##### 5.5.2.10.2 collection\_interval\_start\_date

```
            "collection_interval_start_date": {
              "type": "string",
              "format": "date-time",
              "description": "The UTC date and time where the TrafficSensor data collection started. The averages and totals contained in the TrafficSensor data apply to the inclusive interval of 'collection_interval_start_date' to 'collection_interval_end_date'."
            },
```

##### 5.5.2.10.3 collection\_interval\_end\_date

```
            "collection_interval_end_date": {
              "type": "string",
              "format": "date-time",
              "description": "The UTC date and time where the TrafficSensor data collection ended. The averages and totals contained in the TrafficSensor data apply to the inclusive interval of 'collection_interval_start_date' to 'collection_interval_end_date'."
            },
```

##### 5.5.2.10.4 average\_speed\_kph

```
            "average_speed_kph": {
              "type": "number",
              "minimum": 0,
              "description": "The average speed of vehicles across all lanes over the collection interval in kilometers per hour."
            },
```

##### 5.5.2.10.5 volume\_vph

```
            "volume_vph": {
              "type": "number",
              "minimum": 0,
              "description": "The rate of vehicles passing by the sensor during the collection interval in vehicles per hour."
            },
```

##### 5.5.2.10.6 occupancy\_percent

```
            "occupancy_percent": {
              "type": "number",
              "minimum": 0,
              "description": "The percent of time the roadway section monitored by the sensor was occupied by a vehicle over the collection interval."
            },
```

##### 5.5.2.10.7 lane\_data

```
            "lane_data": {
              "type": "array",
              "items": {
                "$ref": "#/definitions/TrafficSensorLaneData"
              }
            }
          }
        }
      ]
    },
```

#### 5.5.2.11 TrafficSensorLaneData

```
    "TrafficSensorLaneData": {
      "title": "Traffic Sensor Lane Data",
      "description": "Data for a single lane measured by a TrafficSensor deployed on the roadway.",
      "required": [
        "lane_order"
      ],
      "properties": {
```

##### 5.5.2.11.1 lane\_order

```
        "lane_order": {
          "type": "integer",
          "minimum": 1,
          "description": "The lane's position in sequence on the roadway."
        },
```

##### 5.5.2.11.2 road\_event\_id

```
        "road_event_id": {
          "type": "string",
          "description": "The ID of a RoadEventFeature that the measured lane occurs in."
        },
```

##### 5.5.2.11.3 average\_speed\_kph

```
        "average_speed_kph": {
          "type": "number",
          "minimum": 0,
          "description": "The average speed of traffic in the lane over the collection interval (in kilometers per hour)."
        },
```

##### 5.5.2.11.4 volume\_vph

```
        "volume_vph": {
          "type": "number",
          "minimum": 0,
          "description": "The rate of vehicles passing by the sensor in the lane during the collection interval (in vehicles per hour)."
        },
```

##### 5.5.2.11.5 occupancy\_percent

```
        "occupancy_percent": {
          "type": "number",
          "minimum": 0,
          "description": "The percent of time the lane monitored by the sensor was occupied by a vehicle over the collection interval."
        }
      }
    },
```

#### 5.5.2.12 TrafficSignal

```
    "TrafficSignal": {
      "title": "Traffic Signal",
      "description": "Describes a temporary traffic signal deployed on a roadway.",
      "allOf": [
        {
          "properties": {
            "core_details": {
              "properties": {
                "device_type": {
                  "const": "traffic-signal"
                }
              },
              "required": ["device_type"]
            }
          },
          "required": ["core_details"]
        },
        {
          "required": [
            "core_details",
            "mode"
          ],
          "properties": {
```

##### 5.5.2.12.1 core\_details

```
            "core_details": {
              "$ref": "#/definitions/FieldDeviceCoreDetails"
            },
```

##### 5.5.2.12.2 mode

```
            "mode": {
              "$ref": "#/definitions/TrafficSignalMode"
            }
          }
        }
      ]
    },
```

#### 5.5.2.13 RoadsideUnit

```
    "RoadsideUnit": {
      "title": "Roadside Unit",
      "description": "Describes a roadside unit deployed on a roadway.",
      "allOf": [
        {
          "properties": {
            "core_details": {
              "properties": {
                "device_type": {
                  "const": "roadside-unit"
                }
              },
              "required": ["device_type"]
            }
          },
          "required": ["core_details"]
        },
        {
          "required": [
            "core_details"
          ],
          "properties": {
```

##### 5.5.2.13.1 core\_details

```
            "core_details": {
              "$ref": "#/definitions/FieldDeviceCoreDetails"
            },
```

##### 5.5.2.13.2 message\_types

```
            "message_types": {
              "description": "A list of message types being broadcast by a RoadsideUnit.",
              "type": "array",
              "items": {
                "$ref": "#/definitions/RoadsideUnitMessageTypes"
              },
              "uniqueItems": true
            }
          }
        }
      ]
    },
```

#### 5.5.2.14 UnitOfMeasurement

```
    "UnitOfMeasurement": {
      "title": "Unit of Measurement Enumerated Type",
      "description": "Unit of measurement, used when providing a unit to accompany a value.",
      "enum": ["feet", "inches", "centimeters", "pounds", "tons", "kilograms", "miles", "kilometers"]
    },
```

#### 5.5.2.15 ArrowBoardPattern

```
    "ArrowBoardPattern": {
      "title": "Arrow Board Pattern Enumerated Type",
      "description": "A list of options for the posted pattern on an ArrowBoard.",
      "enum": [
        "blank",
        "right-arrow-static",
        "right-arrow-flashing",
        "right-arrow-sequential",
        "right-chevron-static",
        "right-chevron-flashing",
        "right-chevron-sequential",
        "left-arrow-static",
        "left-arrow-flashing",
        "left-arrow-sequential",
        "left-chevron-static",
        "left-chevron-flashing",
        "left-chevron-sequential",
        "bidirectional-arrow-static",
        "bidirectional-arrow-flashing",
        "line-flashing",
        "diamonds-alternating",
        "four-corners-flashing",
        "unknown"
      ]
    },
```

#### 5.5.2.16 FieldDeviceType

```
    "FieldDeviceType": {
      "title": "Field Device Type Enumerated Type",
      "description": "The type of field device.",
      "enum": [
        "arrow-board",
        "camera",
        "dynamic-message-sign",
        "flashing-beacon",
        "hybrid-sign",
        "location-marker",
        "traffic-sensor",
        "traffic-signal",
        "roadside-unit"
      ]
    },
```

#### 5.5.2.17 FieldDeviceStatus

```
    "FieldDeviceStatus": {
      "title": "Field Device Status Enumerated Type",
      "description": "The operational status of a field device.",
      "enum": ["ok", "warning", "error", "unknown"]
    },
```

#### 5.5.2.18 FlashingBeaconFunction

```
    "FlashingBeaconFunction": {
      "title": "Flashing Beacon Function Enumerated Type",
      "description": "Options for what a FlashingBeacon is being used to indicate.",
      "enum": ["vehicle-entering", "queue-warning", "reduced-speed", "workers-present", "other"]
    },
```

#### 5.5.2.19 HybridSignDynamicMessageFunction

```
    "HybridSignDynamicMessageFunction": {
      "title": "Hybrid Sign Dynamic Message Function Enumerated Type",
      "description": "Options for the function of the dynamic message displayed by the electronic display on a HybridSign.",
      "enum": ["speed-limit", "travel-time", "other"]
    },
```

#### 5.5.2.20 MarkedLocationType

```
    "MarkedLocationType": {
      "title": "Marked Location Type Enumerated Type",
      "description": "Options for what a MarkedLocation can mark, such as the start or end of a road event.",
      "enum": [
        "afad",
        "delineator",
        "flagger",
        "lane-shift",
        "lane-closure",
        "personal-device",
        "ramp-closure",
        "road-closure",
        "work-truck-with-lights-flashing",
        "work-zone-start",
        "work-zone-end",
        "attenuator-vehicle",
        "construction-vehicle",
        "maintenance-vehicle",
        "emergency-vehicle",
        "stalled-or-disabled-vehicle",
        "pavement-marking-vehicle",
        "other"
      ]
    },
```

#### 5.5.2.21 TrafficSignalMode

```
    "TrafficSignalMode": {
      "title": "Traffic Signal Mode Enumerated Type",
      "description": "Describes the current operating mode of a TrafficSignal.",
      "enum": [
        "blank",
        "flashing-red",
        "flashing-yellow",
        "fully-actuated",
        "manual",
        "pre-timed",
        "semi-actuated",
        "unknown"
      ]
    },
```

#### 5.5.2.22 RoadsideUnitMessageTypes

```
    "RoadsideUnitMessageTypes": {
      "title": "Roadside Unit Message Types Enumerated Type",
      "description": "Describes the message types being broadcast by a RoadsideUnit.",
      "enum": [
        "rsm",
        "tim",
        "spat",
        "map",
        "other"
      ]
    }
  }
}
```

## 5.6 Direction Schema

```
{
  "$id": "https://raw.githubusercontent.com/ite-org/cwz/main/schemas/1.0/Direction.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Direction Enumerated Type",
  "description": "The direction of a road based on standard naming for US roads; indicates the direction the traffic flow not the real heading angle.",
  "enum": ["northbound", "eastbound", "southbound", "westbound", "inner-loop", "outer-loop", "undefined", "unknown"]
}
```

## 5.7 BoundingBox Schema

​```
{
  "$id": "https://raw.githubusercontent.com/ite-org/cwz/main/schemas/1.0/BoundingBox.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "GeoJSON Bounding Box",
  "description": "Information on the coordinate range for a Geometry, Feature, or FeatureCollection.",
  "type": "array",
  "minItems": 4,
  "items": {
    "type": "number"
  }
}
```