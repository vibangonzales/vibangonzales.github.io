# **Annex A** 

# **Protocol Requirements List Table (PRL)**

In addition to the Conformance and Support columns discussed in Sections 3.10.1.1 and 3.10.1.3, the PRL table contains columns for the Need ID, Need, Req ID, Requirements, Conformance, Support, and Additional Specifications. These are described as follows:

* **Need ID.** The number assigned to the user need statement. The needs are defined within Section 2 and the PRL is based upon the user needs within that Section.
* **Need.** A short descriptive title identifying the user need.
* **Req ID.** The number assigned to the requirement statement. The requirements are defined within Section 3, and the PRL traces the relationship between needs and the corresponding requirements.
* **Requirement.** A short descriptive title identifying the requirement.
* **Conformance.** Identifies whether the requirement is mandatory or optional, and notes any conformance dependencies.
* **Support.** Used by specification developers to identify whether the requirement should be supported.
* **Additional Specifications.** Identifies other requirements to satisfy, including user-selectable range values. The "Additional Specifications" column may (and should) be used in procurement specifications to provide additional notes and requirements for the product to be procured or by an implementer to detail the implementation. In some cases, default text may already exist in this field and should be completed to fully specify the equipment. Additional text can be added to this field as needed to further detail a feature.

## Table 6. Protocol Requirements List

|**Need ID**|**Need**|**Req ID**|**Requirement**|**Conformance**|**Support**|**Additional Specifications**|
|-|-|-|-|-|-|-|
|**2.5.1**|[**Architectural Needs**](concept-of-operations.md/#251-architectural-needs)||||||
|**2.5.1.1**|[**Compatibility with the WZDx Specification**](concept-of-operations.md/#2511-architectural-need-compatibility-with-the-wzdx-specification)||||||
|||**3.2**|[**Architectural Requirements**](system-requirements.md/#32-architectural-requirements)| | | |
|||**3.2.1**|[**Compatibility with the WZDx Specification**](system-requirements.md/#321-compatibility-with-the-wzdx-specification)|M|Yes| |
|||**3.2.2**|[**GeoJSON Data Format**](system-requirements.md/#322-geojson-data-format)|M|Yes| |
|||**3.2.3**|[**GeoJSON Data Validation**](system-requirements.md/#323-geojson-data-validation)|M|Yes| |
|||**3.2.4**|[**Business Rules**](system-requirements.md/#324-business-rules)|**M**|**Yes**||
|||3.2.4.1|[Event Segments Follow Attribute Changes](system-requirements.md/#3241-event-segments-follow-attribute-changes)|M|Yes||
|||3.2.4.2|[WorkZoneRoadEvent Lanes](system-requirements.md/#3242-workzoneroadevent-lanes)|M|Yes||
|||3.2.4.3|[Lane Order](system-requirements.md/#3243-lane-order)|M|Yes||
|||3.2.4.4|[Data Source ID Referential Integrity](system-requirements.md/#3244-data-source-id-referential-integrity)|M|Yes||
|||3.2.4.5|[UTC Date-Time Format Specification](system-requirements.md/#3245-utc-date-time-format-specification)|M|Yes||
|||3.2.4.6|[UUID Format Specification](system-requirements.md/#3246-uuid-format-specification)|M|Yes||
|||**3.5.1**|[**Contents of FeedInfo**](system-requirements.md/#351-contents-of-feedinfo)| | | |
|||3.5.1 f)|[version](system-requirements.md/#351f)|M|Yes||
|||**3.3**|[**Data Exchange Requirements**](system-requirements.md/#33-data-exchange-requirements)| | | |
|||**3.3.1**|[**Exchange WorkZoneFeed Information**](system-requirements.md/#331-exchange-workzonefeed-information)| | | |
|||3.3.1.1|[Send WorkZoneFeed Information Upon Requestdir|M|Yes| |
|||**3.3.2**|[**Exchange DeviceFeed Information**](system-requirements.md/#332-exchange-devicefeed-information)| | | |
|||3.3.2.1|[Send DeviceFeed Information Upon Request](system-requirements.md/#3321-send-devicefeed-upon-request)|M|Yes| |
|||**3.4**|[**WorkZoneFeed Requirements**](system-requirements.md/#34-workzonefeed-requirements)| | | |
|||**3.4.1**|[**Contents of WorkZoneFeed**](system-requirements.md/#341-contents-of-workzonefeed)| | | |
|||3.4.1 a)|[feed\_info](system-requirements.md/#341a)|M|Yes| |
|||3.4.1 b)|[type](system-requirements.md/#341b)|M|Yes| |
|||3.4.1 c)|[features](system-requirements.md/#341c)|M|Yes| |
|||3.4.1 d)|[bbox](system-requirements.md/#341d)|O|Yes / No| |
|||**3.5**|[**FeedInfo Requirements**](system-requirements.md/#35-feedinfo-requirements)| | | |
|||**3.5.1**|[**Contents of FeedInfo**](system-requirements.md/#351-contents-of-feedinfo)| | | |
|||3.5.1 a)|[publisher](system-requirements.md/#351a)|M|Yes| |
|||3.5.1 b)|[contact\_name](system-requirements.md/#351b)|O|Yes / No| |
|||3.5.1 c)|[contact\_email](system-requirements.md/#351c)|O|Yes / No| |
|||3.5.1 d)|[update\_frequency](system-requirements.md/#351d)|O|Yes / No| |
|||3.5.1 e)|[update\_date](system-requirements.md/#351e)|M|Yes| |
|||3.5.1 f)|[version](system-requirements.md/#351f)|M|Yes| |
|||3.5.1 g)|[license](system-requirements.md/#351g)|O|Yes / No| |
|||3.5.1 h)|[data\_sources](system-requirements.md/#351h)|M|Yes| |
|||**3.5.2**|**Contents of FeedDataSource**| | | |
|||3.5.2 a)|[data\_source\_id](system-requirements.md/#352a)|M|Yes| |
|||3.5.2 b)|[organization\_name](system-requirements.md/#352b)|M|Yes| |
|||3.5.2 c)|[contact\_name](system-requirements.md/#352c)|O|Yes / No| |
|||3.5.2 d)|[contact\_email](system-requirements.md/#352d)|O|Yes / No| |
|||3.5.2 e)|[update\_frequency](system-requirements.md/#352e)|M|Yes| |
|||3.5.2 f)|[update\_date](system-requirements.md/#352f)|M|Yes| |
|||**3.6**|**RoadEventFeature Requirements**| | | |
|||**3.6.1**|**Contents of RoadEventFeature**| | | |
|||3.6.1 a)|[id](system-requirements.md/#361a)|M|Yes| |
|||3.6.1 b)|[type](system-requirements.md/#361b)|M|Yes| |
|||3.6.1 c)|[properties](system-requirements.md/#361c)|M|Yes| |
|||3.6.1 d)|[geometry](system-requirements.md/#361d)|M|Yes| |
|||3.6.1 e)|[bbox](system-requirements.md/#361e)|O|Yes / No| |
|||**3.6.2**|**Contents of WorkZoneRoadEvent**| | | |
|||3.6.2 a)|[core\_details](system-requirements.md/#362a)|M|Yes| |
|||3.6.2 b)|[beginning\_cross\_street](system-requirements.md/#362b)|O|Yes / No| |
|||3.6.2 c)|[ending\_cross\_street](system-requirements.md/#362c)|O|Yes / No| |
|||3.6.2 d)|[beginning\_reference\_post](system-requirements.md/#362d)|O|Yes / No| |
|||3.6.2 e)|[ending\_reference\_post](system-requirements.md/#362e)|O|Yes / No| |
|||3.6.2 f)|[reference\_post\_unit](system-requirements.md/#362f)|RefPost:O|Yes / No||
|||3.6.2 g)|[is\_start\_position\_verified](system-requirements.md/#362g)|M|Yes| |
|||3.6.2 h)|[is\_end\_position\_verified](system-requirements.md/#362h)|M|Yes| |
|||3.6.2 i)|[start\_date](system-requirements.md/#362i)|M|Yes| |
|||3.6.2 j)|[end\_date](system-requirements.md/#362j)|M|Yes| |
|||3.6.2 k)|[is\_start\_date\_verified](system-requirements.md/#362k)|M|Yes| |
|||3.6.2 l)|[is\_end\_date\_verified](system-requirements.md/#362l)|M|Yes| |
|||3.6.2 m)|[work\_zone\_type](system-requirements.md/#362m)|O|Yes / No| |
|||3.6.2 n)|[vehicle\_impact](system-requirements.md/#362n)|M|Yes| |
|||3.6.2 o)|[location\_method](system-requirements.md/#362o)|M|Yes| |
|||3.6.2 p)|[worker\_presence](system-requirements.md/#362p)|O|Yes / No| |
|||3.6.2 q)|[reduced\_speed\_limit\_kph](system-requirements.md/#362q)|O|Yes / No| |
|||3.6.2 r)|[restrictions](system-requirements.md/#362r)|O|Yes / No| |
|||3.6.2 s)|[types\_of\_work](system-requirements.md/#362s)|O|Yes / No| |
|||3.6.2 t)|[lanes](system-requirements.md/#362t)|O|Yes / No| |
|||3.6.2 u)|[impacted\_cds\_curb\_zones](system-requirements.md/#362u)|O|Yes / No| |
|||**3.6.3**|**Contents of DetourRoadEvent**| | | |
|||3.6.3 a)|[core\_details](system-requirements.md/#363a)|M|Yes| |
|||3.6.3 b)|[beginning\_cross\_street](system-requirements.md/#363b)|O|Yes / No| |
|||3.6.3 c)|[ending\_cross\_street](system-requirements.md/#363c)|O|Yes / No| |
|||3.6.3 d)|[beginning\_reference\_post](system-requirements.md/#363d)|O|Yes / No| |
|||3.6.3 e)|[ending\_reference\_post](system-requirements.md/#363e)|O|Yes / No| |
|||3.6.3 f)|[reference\_post\_unit](system-requirements.md/#363f)|RefPost:O|Yes / No||
|||3.6.3 g)|[start\_date](system-requirements.md/#363g)|M|Yes| |
|||3.6.3 h)|[end\_date](system-requirements.md/#363h)|M|Yes| |
|||3.6.3 i)|[is\_start\_date\_verified](system-requirements.md/#363i)|M|Yes| |
|||3.6.3 j)|[is\_end\_date\_verified](system-requirements.md/#363j)|M|Yes| |
|||**3.6.4**|**Contents of RoadEventCoreDetails**| | | |
|||3.6.4 a)|[data\_source\_id](system-requirements.md/#364a)|M|Yes| |
|||3.6.4 b)|[event\_type](system-requirements.md/#364b)|M|Yes| |
|||3.6.4 c)|[related\_road\_events](system-requirements.md/#364c)|O|Yes / No| |
|||3.6.4 d)|[road\_names](system-requirements.md/#364d)|M|Yes| |
|||3.6.4 e)|[direction](system-requirements.md/#364e)|M|Yes| |
|||3.6.4 f)|[name](system-requirements.md/#364f)|O|Yes / No| |
|||3.6.4 g)|[description](system-requirements.md/#364g)|O|Yes / No| |
|||3.6.4 h)|[creation\_date](system-requirements.md/#364h)|O|Yes / No| |
|||3.6.4 i)|[update\_date](system-requirements.md/#364i)|O|Yes / No| |
|||**3.6.5**|**Enumeration of LocationMethod**|**NA**| | |
|||**3.6.6**|**Contents of RelatedRoadEvent**| | | |
|||3.6.6 a)|[type](system-requirements.md/#366a)|M|Yes| |
|||3.6.6 b)|[id](system-requirements.md/#366b)|M|Yes| |
|||**3.6.7**|**Contents of TypeOfWork**| | | |
|||3.6.7 a)|[type\_name](system-requirements.md/#367a)|M|Yes| |
|||3.6.7 b)|[is\_architectural\_change](system-requirements.md/#367b)|O|Yes / No| |
|||**3.6.8**|**Contents of Lane**| | | |
|||3.6.8 a)|[order](system-requirements.md/#368a)|M|Yes| |
|||3.6.8 b)|[status](system-requirements.md/#368b)|M|Yes| |
|||3.6.8 c)|[type](system-requirements.md/#368c)|M|Yes| |
|||3.6.8 d)|[restrictions](system-requirements.md/#368d)|O|Yes / No| |
|||**3.6.9**|**Contents of Restriction**| | | |
|||3.6.9 a)|[type](system-requirements.md/#369a)|M|Yes| |
|||3.6.9 b)|[value](system-requirements.md/#369b)|O|Yes / No| |
|||3.6.9 c)|[unit](system-requirements.md/#369c)|ResValue:O|Yes / No| |
|||**3.6.10**|**Contents of CdsCurbZonesReference**| | | |
|||3.6.10 a)|[cds\_curb\_zone\_ids](system-requirements.md/#3610a)|M|Yes| |
|||3.6.10 b)|[cds\_curbs\_api\_url](system-requirements.md/#3610b)|M|Yes| |
|||**3.6.11**|**Contents of WorkerPresence**| | | |
|||3.6.11 a)|[are\_workers\_present](system-requirements.md/#3611a)|M|Yes| |
|||3.6.11 b)|[method](system-requirements.md/#3611b)|O|Yes / No| |
|||3.6.11 c)|[worker\_presence\_last\_confirmed\_date](system-requirements.md/#3611c)|O|Yes / No| |
|||3.6.11 d)|[confidence](system-requirements.md/#3611d)|O|Yes / No| |
|||**3.6.12**|**Enumeration of EventType**|**NA**| | |
|||**3.6.13**|**Enumeration of WorkZoneType**|**NA**| | |
|||**3.6.14**|**Enumeration of VehicleImpact**|**NA**| | |
|||**3.6.15**|**Enumeration of RestrictionType**|**NA**| | |
|||**3.6.16**|**Enumeration of WorkTypeName**|**NA**| | |
|||**3.6.17**|**Enumeration of LaneStatus**|**NA**| | |
|||**3.6.18**|**Enumeration of LaneType**|**NA**| | |
|||**3.6.19**|**Enumeration of UnitOfMeasurement**|**NA**| | |
|||**3.6.20**|**Enumeration of WorkerPresenceMethod**|**NA**| | |
|||**3.6.21**|**Enumeration of WorkerPresenceDefinition**|**NA**| | |
|||**3.6.22**|**Enumeration of WorkerPresenceConfidence**|**NA**| | |
|||**3.6.23**|**Enumeration of RelatedRoadEventType**|**NA**| | |
|||**3.7**|**DeviceFeed Requirements**| | | |
|||**3.7.1**|**Contents of DeviceFeed**| | | |
|||3.7.1 a)|feed\_info|M|Yes| |
|||3.7.1 b)|type|M|Yes| |
|||3.7.1 c)|features|M|Yes| |
|||3.7.1 d)|bbox|O|Yes / No| |
|||**3.7.2**|**Contents of FieldDeviceFeature**| | | |
|||3.7.2 a)|id|M|Yes| |
|||3.7.2 b)|type|M|Yes| |
|||3.7.2 c)|properties|M|Yes| |
|||3.7.2 d)|geometry|M|Yes| |
|||3.7.2 e)|bbox|O|Yes / No| |
|||**3.7.3**|**Contents of FieldDeviceCoreDetails**| | | |
|||3.7.3 a)|device\_type|M|Yes| |
|||3.7.3 b)|data\_source\_id|M|Yes| |
|||3.7.3 c)|device\_status|M|Yes| |
|||3.7.3 d)|update\_date|M|Yes| |
|||3.7.3 e)|has\_automatic\_location|M|Yes| |
|||3.7.3 f)|road\_direction|O|Yes / No| |
|||3.7.3 g)|road\_names|O|Yes / No| |
|||3.7.3 h)|name|O|Yes / No| |
|||3.7.3 i)|description|O|Yes / No| |
|||3.7.3 j)|status\_messages|O|Yes / No| |
|||3.7.3 k)|is\_moving|O|Yes / No| |
|||3.7.3 l)|road\_event\_ids|O|Yes / No| |
|||3.7.3 m)|reference\_post|O|Yes / No| |
|||3.7.3 n)|reference\_post\_unit|RefPost:O|Yes / No||
|||3.7.3 o)|make|O|Yes / No| |
|||3.7.3 p)|model|O|Yes / No| |
|||3.7.3 q)|serial\_number|O|Yes / No| |
|||3.7.3 r)|firmware\_version|O|Yes / No| |
|||3.7.3 s)|velocity\_kph|O|Yes / No| |
|||3.7.3 t)|is\_in\_transport\_position|O|Yes / No| |
||||||||
|||**3.7.4**|**Contents of ArrowBoard**| | | |
|||3.7.4 a)|core\_details|M|Yes| |
|||3.7.4 b)|pattern|M|Yes| |
|||**3.7.5**|**Contents of Camera**| | | |
|||3.7.5 a)|core\_details|M|Yes| |
|||3.7.5 b)|image\_url|O|Yes / No| |
|||3.7.5 c)|is\_image\_url\_public|O|Yes / No| |
|||3.7.5 d)|image\_timestamp|ImgURL:O|Yes / No| |
|||3.7.5 e)|video\_url|O|Yes / No||
|||3.7.5 f)|is\_video\_url\_public|O|Yes / No| |
|||3.7.5 g)|video\_update\_frequency|VideoUrl:O|Yes / No||
|||**3.7.6**|**Contents of DynamicMessageSign**| | | |
|||3.7.6 a)|core\_details|M|Yes| |
|||3.7.6 b)|message\_multi\_string|M|Yes| |
|||**3.7.7**|**Contents of FlashingBeacon**| | | |
|||3.7.7 a)|core\_details|M|Yes| |
|||3.7.7 b)|function|M|Yes| |
|||3.7.7 c)|is\_flashing|O|Yes / No| |
|||3.7.7 d)|sign\_text|O|Yes / No| |
|||**3.7.8**|**Contents of HybridSign**| | | |
|||3.7.8 a)|core\_details|M|Yes| |
|||3.7.8 b)|dynamic\_message\_function|M|Yes| |
|||3.7.8 c)|dynamic\_message\_text|O|Yes / No| |
|||3.7.8 d)|static\_sign\_text|O|Yes / No| |
|||**3.7.9**|**Contents of LocationMarker**| | | |
|||3.7.9 a)|core\_details|M|Yes| |
|||3.7.9 b)|marked\_locations|M|Yes| |
|||**3.7.10**|**Contents of MarkedLocation**| | | |
|||3.7.10 a)|type|M|Yes| |
|||3.7.10 b)|road\_event\_id|O|Yes / No| |
|||**3.7.11**|**Contents of TrafficSensor**| | | |
|||3.7.11 a)|core\_details|M|Yes| |
|||3.7.11 b)|collection\_interval\_start\_date|M|Yes| |
|||3.7.11 c)|collection\_interval\_end\_date|M|Yes| |
|||3.7.11 d)|average\_speed\_kph|O|Yes / No| |
|||3.7.11 e)|volume\_vph|O|Yes / No| |
|||3.7.11 f)|occupancy\_percent|O|Yes / No| |
|||3.7.11 g)|lane\_data|O|Yes / No| |
|||**3.7.12**|**Contents of TrafficSensorLaneData**| | | |
|||3.7.12 a)|lane\_order|M|Yes| |
|||3.7.12 b)|road\_event\_id|O|Yes / No| |
|||3.7.12 c)|average\_speed\_kph|O|Yes / No| |
|||3.7.12 d)|volume\_vph|O|Yes / No| |
|||3.7.12 e)|occupancy\_percent|O|Yes / No| |
|||**3.7.13**|**Contents of TrafficSignal**| | | |
|||3.7.13 a)|core\_details|M|Yes| |
|||3.7.13 b)|mode|M|Yes| |
|||**3.7.16**|**Enumeration of ArrowBoardPattern**|**NA**| | |
|||**3.7.17**|**Enumeration of FieldDeviceType**|**NA**| | |
|||**3.7.18**|**Enumeration of FieldDeviceStatus**|**NA**| | |
|||**3.7.19**|**Enumeration of FlashingBeaconFunction**|**NA**| | |
|||**3.7.20**|**Enumeration of HybridSignDynamicMessageFunction**|**NA**| | |
|||**3.7.21**|**Enumeration of MarkedLocationType**|**NA**| | |
|||**3.7.22**|**Enumeration of TrafficSignalMode**|**NA**| | |
|||**3.8**|**Direction Requirements**| | | |
|||**3.8.1**|**Enumeration of Direction**|**NA**| | |
|||**3.9**|**BoundingBox Requirements**| | | |
|||**3.9.1**|**Contents of BoundingBox**|**O**| | |
|**2.5.1.2**|[**GeoJSON Data Exchange**](concept-of-operations.md/#2512-architectural-need-geojson-data-exchange-constraint)||||||
|**2.5.1.2.1**|**Poll for Data**| | | | | |
|||3.3.1.1|Send WorkZoneFeed Information Upon Request|M|Yes| |
|||3.3.2.1|Send DeviceFeed Information Upon Request|M|Yes| |
|**2.5.1.3**|**GeoJSON Data Format**| | | | | |
|||**3.2.3**|**GeoJSON Data Format**|M|Yes| |
|**2.5.1.4**|**GeoJSON Data Validation**||||||
|||**3.2.4**|**GeoJSON Data Validation**|M|Yes| |
|**2.5.1.5**|**Frequency of Updates**| | | | | |
|||**3.5.2**|**Contents of FeedDataSource**|M|Yes| |
|||3.5.2 e)|update\_frequency|M|Yes| |
|||3.5.2 f)|update\_date|M|Yes| |
|**2.5.1.6**|**UTC Date-Time Format Specification**| | | | | |
|||3.2.4.5|UTC Date-Time Format Specification|M|Yes| |
|**2.5.2**|**Data Exchange Needs**| | | | | |
|**2.5.2.1**|**Zone Metadata**| | | | | |
|2.5.2.1.1|Zone Data Standard Version||||||
|||**3.5.1**|**Contents of FeedInfo**| | | |
|||3.5.1 f)|version|M|Yes| |
|2.5.2.1.2|Zone Identifier| | | | | |
|2.5.2.1.2.1|Support Zone Identifier for Zones| | | | | |
|||3.2.4.4|Data Source ID Referential Integrity|M|Yes||
|||3.2.4.6|UUID Format Specification|M|Yes||
|||**3.6.1**|**Contents of RoadEventFeature**| | | |
|||3.6.1 a)|id|M|Yes| |
|2.5.2.1.2.2|Support Unique Zone Identifiers| | | | | |
|||3.2.4.6|UUID Format Specification|M|Yes||
|||**3.6.1**|**Contents of RoadEventFeature**| | | |
|||3.6.1 a)|id|M|Yes| |
|2.5.2.1.2.3|Support Unique Zone Group Identifiers||||||
|||**3.6.4**|**Contents of RoadEventCoreDetails**| | ||
|||3.6.4 c)|project\_id|O|Yes / No| |
|||**3.7.3**|**Contents of FieldDeviceCoreDetails**| | ||
|||3.7.3 m)|project\_id|O|Yes / No| |
|2.5.2.1.2.4|Zone Identifier for VRUs, Devices, Work Zone Vehicles, Lanes, Speed Limit Zones||||||
|||3.2.4.6|UUID Format Specification|M|Yes||
|||**3.6.1**|**Contents of RoadEventFeature**| | | |
|||3.6.1 a)|id|M|Yes| |
|2.5.2.1.3|Zone Activity Type| | | | | |
|||**3.6.2**|**Contents of WorkZoneRoadEvent**| | | |
|||3.6.2 s)|types\_of\_work|O|Yes / No| |
|2.5.2.1.4|Zone Data Timestamp| | | | | |
|||**3.6.4**|**Contents of RoadEventCoreDetails**| | | |
|||3.6.4 h)|creation\_date|O|Yes / No| |
|||3.6.4 i)|update\_date|O|Yes / No| |
|2.5.2.1.5|Zone Data Source| | | | | |
|||3.2.4.4|Data Source ID Referential Integrity|M|Yes||
|||**3.5.1**|**Contents of FeedInfo**| | | |
|||3.5.1 h)|data\_sources|M|Yes| |
|||**3.6.4**|**Contents of RoadEventCoreDetails**| | | |
|||3.6.4 a)|data\_source\_id|M|Yes| |
|**2.5.2.2**|**Zone Location**| | | | | |
|2.5.2.2.1|Zone Geometry| | | | | |
|||3.2.4.1|Event Segments Follow Attribute Changes|M|Yes||
|||**3.6.1**|**Contents of RoadEventFeature**| | | |
|||3.6.1 d)|geometry|M|Yes| |
|||**3.6.2**|**Contents of WorkZoneRoadEvent**| | | |
|||3.6.2 g)|is\_start\_position\_verified|M|Yes| |
|||3.6.2 h)|is\_end\_position\_verified|M|Yes| |
|**2.5.2.3**|**Zone Schedule**| | | | | |
|2.5.2.3.1|Date Times| | | | | |
|||**3.6.2**|**Contents of WorkZoneRoadEvent**| | | |
|||3.6.2 i)|start\_date|M|Yes| |
|||3.6.2 j)|end\_date|M|Yes| |
|||3.6.2 k)|is\_start\_date\_verified|M|Yes| |
|||3.6.2 l)|is\_end\_date\_verified|M|Yes| |
|**2.5.2.4**|**Zone Segmentation**| | | | | |
|2.5.2.4.1|Geometry| | | | | |
|||**3.6.4**|**Contents of RoadEventCoreDetails**| | | |
|||3.6.4 c)|project\_id|O|Yes / No| |
|||**3.7.3**|**Contents of FieldDeviceCoreDetails**| | | |
|||3.7.3 m)|project\_id|O|Yes / No||
|2.5.2.4.2|Date Times| | | | | |
|||**3.6.4**|**Contents of RoadEventCoreDetails**| | | |
|||3.6.4 c)|project\_id|O|Yes / No| |
|||**3.7.3**|**Contents of FieldDeviceCoreDetails**| | | |
|||3.7.3 m)|project\_id|O|Yes / No||
|**2.5.2.5**|**Zone Status**| | | | | |
|2.5.2.5.1|Is Active| | | | | |
|||**3.6.2**|**Contents of WorkZoneRoadEvent**| | | |
|||3.6.2 k)|is\_start\_date\_verified|M|Yes| |
|||3.6.2 l)|is\_end\_date\_verified|M|Yes| |
|2.5.2.5.2|Length| | | | | |
|||**3.6.1**|**Contents of RoadEventFeature**| | | |
|||3.6.1 d)|geometry|M|Yes|Calculated using coordinate information contained in the linestring|
|2.5.2.5.3|Number of Lanes Open| | | | | |
|||**3.6.8**|**Contents of Lane**| | | |
|||3.6.8 b)|status|M|Yes| |
|||**3.6.17**|**Enumeration of LaneStatus**| | | |
|2.5.2.5.4|Ad-hoc (Unscheduled/Unplanned)||||||
|||**3.6.14**|**Enumeration of VehicleImpact**| | | |
|||**3.6.15**|**Enumeration of RestrictionType**||||
|2.5.2.5.5|Is Rolling/Moving| | | | | |
|||**3.6.2**|**Contents of WorkZoneRoadEvent**| | | |
|||3.6.2 m)|work\_zone\_type|O|Yes / No| |
|||**3.6.8**|**Contents of Lane**| | | |
|||3.6.8 a)|order|M|Yes| |
|||**3.6.13**|**Enumeration of WorkZoneType**| | | |
|**2.5.2.6**|**Zone Lanes**| | | | | |
|2.5.2.6.1|Numbering and Identification||||||
|||3.2.4.2|WorkZoneRoadEvent Lanes|M|Yes| |
|2.5.2.6.1.1|Nationally Consistent Method of Lane Numbering||||||
|||3.2.4.3|Lane Order|M|Yes||
|||**3.6.2**|**Contents of WorkZoneRoadEvent**| | | |
|||3.6.2 t)|lanes|O|Yes / No| |
|||**3.6.8**|**Contents of Lane**| | | |
|||3.6.8 a)|order|M|Yes| |
|2.5.2.6.1.2|Lane Numbering is Left-to-Right or Right-to-Left||||||
|||**3.6.2**|**Contents of WorkZoneRoadEvent**| | | |
|||3.6.2 t)|lanes|O|Yes / No| |
|||**3.6.8**|**Contents of Lane**| | | |
|||3.6.8 a)|order|M|Yes| |
|2.5.2.6.2|Lane Type| | | | | |
|||**3.6.2**|**Contents of WorkZoneRoadEvent**| | | |
|||3.6.2 t)|lanes|O|Yes / No| |
|||**3.6.8**|**Contents of Lane**| | | |
|||3.6.8 a)|order|M|Yes| |
|||3.6.8 c)|type|M|Yes| |
|||**3.6.17**|**Enumeration of LaneStatus**| | | |
|||**3.6.18**|**Enumeration of LaneType**| | | |
|2.5.2.6.2.1|Lane is Drivable| | | | | |
|||**3.6.2**|**Contents of WorkZoneRoadEvent**| | | |
|||3.6.2 t)|lanes|O|Yes / No| |
|||**3.6.8**|**Contents of Lane**| | | |
|||3.6.8 a)|order|M|Yes| |
|||3.6.8 c)|type|M|Yes| |
|||**3.6.17**|**Enumeration of LaneStatus**| | | |
|||**3.6.18**|**Enumeration of LaneType**| | | |
|2.5.2.6.2.2|Special Use Lane| | | | | |
|||**3.6.2**|**Contents of WorkZoneRoadEvent**| | | |
|||3.6.2 t)|lanes|O|Yes / No| |
|||**3.6.8**|**Contents of Lane**| | | |
|||3.6.8 a)|order|M|Yes| |
|||3.6.8 c)|type|M|Yes| |
|||**3.6.17**|**Enumeration of LaneStatus**| | | |
|||**3.6.18**|**Enumeration of LaneType**| | | |
|2.5.2.6.2.3|Reversible Lane| | | | | |
|||**3.6.2**|**Contents of WorkZoneRoadEvent**| | | |
|||3.6.2 t)|lanes|O|Yes / No| |
|||**3.6.8**|**Contents of Lane**| | | |
|||3.6.8 a)|order|M|Yes| |
|||3.6.8 c)|type|M|Yes| |
|||**3.6.17**|**Enumeration of LaneStatus**| | | |
|||**3.6.18**|**Enumeration of LaneType**| | | |
|2.5.2.6.3|CVE Roadside Safety Applications||||| |
|||**3.6.1**|**Contents of RoadEventFeature**| | | |
|||3.6.1 d)|geometry|M|Yes| |
|||**3.7.14**|**Contents of RoadsideUnit**||||
|||3.7.14 b)|message\_types|O|Yes / No||
|2.5.2.6.4|Lane Tapers| | | | | |
|||3.2.4.1|Event Segments Follow Lane Geometry Changes|M|Yes||
|||**3.6.2**|**Contents of WorkZoneRoadEvent**| | | |
|||3.6.2 n)|vehicle\_impact|M|Yes| |
|||**3.6.17**|**Enumeration of LaneStatus**| | | |
|2.5.2.6.5|Lane Closure Status| | | | | |
|||**3.6.2**|**Contents of WorkZoneRoadEvent**| | | |
|||3.6.2 t)|lanes|O|Yes / No| |
|||**3.6.8**|**Contents of Lane**| | | |
|||3.6.8 a)|order|M|Yes| |
|||3.6.8 b)|status|M|Yes| |
|||**3.6.17**|**Enumeration of LaneStatus**| | | |
|**2.5.2.7**|**Zone Speed Limit**| | | | | |
|2.5.2.7.1|Position/Geometry| | | | | |
|||**3.6.1**|**Contents of RoadEventFeature**| | | |
|||3.6.1 d)|geometry|M|Yes| |
|2.5.2.7.2|Speed Limit Change| | | | | |
|||**3.6.2**|**Contents of WorkZoneRoadEvent**| | | |
|||3.6.2 q)|reduced\_speed\_limit\_kph|O|Yes / No| |
|**2.5.2.8**|**Zone Traffic Data**| | | | | |
|2.5.2.8.1|Speed, Volume, and Occupancy| | | | | |
|||**3.7.11**|**Contents of Traffic Sensor**| | | |
|||3.7.11 d)|average\_speed\_kph|O|Yes / No| |
|||3.7.11 e)|volume\_vph|O|Yes / No| |
|||3.7.11 f)|occupancy\_percent|O|Yes / No| |
|2.5.2.8.2|Queue Warning| | | | | |
|||**3.7.17**|**Enumeration of FlashingBeaconFunction**| | | |
|**2.5.2.9**|**Zone Device**| | | | | |
|2.5.2.9.1|Inventory and Status| | | | | |
|||**3.7.2**|**Contents of FieldDeviceFeature**| | | |
|||3.7.2 d)|geometry|M|Yes| |
|||**3.7.3**|**Contents of FieldDeviceCoreDetails**| | | |
|||3.7.3 a)|device\_type|M|Yes| |
|||3.7.3 c)|device\_status|M|Yes| |
|||3.7.3 l)|road\_event\_ids|O|Yes / No| |
|||**3.7.17**|**Enumeration of FieldDeviceType**| | | |
|||**3.7.18**|**Enumeration of FieldDeviceStatus**| | | |
|||**3.7.21**|**Enumeration of MarkedLocationType**| | | |
|2.5.2.9.2|Location Marker Type| | | | | |
|||**3.7.21**|**Enumeration of MarkedLocationType**| | | |
|2.5.2.9.3|Device Type| | | | | |
|||**3.7.3**|**Contents of FieldDeviceCoreDetails**| | | |
|||3.7.3 a)|device\_type|M|Yes||
|||**3.7.17**|**Enumeration of FieldDeviceType**| | | |
|2.5.2.9.4|Position/Geometry| | | | | |
|||**3.7.2**|**Contents of FieldDeviceFeature**| | | |
|||3.7.2 d)|geometry|M|Yes| |
|2.5.2.9.5|Device Status| | | | | |
|||**3.7.3**|**Contents of FieldDeviceCoreDetails**| | | |
|||3.7.3 c)|device\_status|M|Yes| |
|||**3.7.18**|**Enumeration of FieldDeviceStatus**| | | |
|2.5.2.9.6|Zone Identifier| | | | | |
|||**3.7.3**|**Contents of FieldDeviceCoreDetails**| | | |
|||3.7.3 l)|road\_event\_ids|O|Yes / No| |
|**2.5.2.10**|**Zone VRU Device**| | | | | |
|2.5.2.10.1|Worker Presence Status/Activity||||||
|||**3.6.2**|**Contents of WorkZoneRoadEvent**| | | |
|||3.6.2 o)|worker\_presence|O|Yes / No| |
|||**3.6.11**|**Contents of WorkerPresence**| | | |
|||3.6.11 a)|are\_workers\_present|M|Yes| |
|||3.6.11 b)|method|O|Yes / No| |
|||3.6.11 c)|worker\_presence\_last\_confirmed\_date|O|Yes / No| |
|||3.6.11 d)|confidence|O|Yes / No||
|||3.6.11 e)|definition|O|Yes / No| |
|||3.6.11 f)|other\_method|WorkerMethod:O|Yes / No||
|2.5.2.10.2|VRU Position/Geometry| | | | | |
|||**3.7.2**|**Contents of FieldDeviceFeature**| | | |
|||3.7.2 d)|Geometry|M|Yes| |
|||**3.7.21**|**Enumeration of MarkedLocationType**| | | |
|**2.5.2.11**|**Zone Work Vehicle Device**| | | | | |
|2.5.2.11.1|Vehicle Type| || | | |
|||**3.7.21**|**Enumeration of MarkedLocationType**| | | |
||| | | | | |
|2.5.2.11.2|Vehicle Position| | | | | |
|||**3.7.2**|**Contents of FieldDeviceFeature**| | | |
|||3.7.2 d)|geometry|M|Yes| |
|||**3.7.21**|**Enumeration of MarkedLocationType**| | | |
||| | | | | |

