# **Annex B** 

# **Requirements Traceability Matrix (RTM)**

##B.1 Notation \[Informative]

###B.1.1 Requirement Columns

The requirements are defined within Section 3, and the RTM is derived from those requirements. The section number and the functional requirement name are indicated within these columns.

###B.1.2 Design Details

The "Design Details" column provides one of the following:

* a hyperlinked reference to a section number in Section 4 or Section 5 where the design details are defined.
* an external, normative reference detailing how to fulfill the requirement.
* The phrase "No Further Design Details" because no additional design information is necessary (i.e., the requirement is self-explanatory).

###B.1.3 Additional Specifications

The "Additional Specifications" column may be used to provide additional notes and requirements or may be used by an implementer to provide any additional details about the implementation.

###B.1.4 Instructions for Completing the RTM \[Informative]

To find the conformant design content for a requirement, search for the requirement identification (section) number or name under the appropriate column. Next to the functional requirements column are columns that define the conformant design details that fulfill the requirement. The columns either reference a section within this standard describing how the requirement is to be fulfilled; points to a normative reference that explains how to fulfill the requirement; or indicates "No Further Design Details" because no additional design information is necessary. The "Additional Specifications" column provides additional notes or details about the design content, as needed.

##B.2 Requirements Traceability Matrix Table

Table 7. Requirements Traceability Matrix

|**Req ID**|**Requirement**|**Data Concept Type**|**Data Concept ID**|**Data Concept Name**|
|-|-|-|-|-|
|**3.2**|[**Architectural Requirements**](system-requirements.md/#32-architectural-requirements)| | | |
|**3.2.1**|[**Compatibility with the WZDx Specification**](system-requirements.md/#321-compatibility-with-the-wzdx-specification)|**Dialog**|**4.2**|[Poll for Data Dialog](dialogs.md/#42-poll-for-data-dialog)|
|**3.2.2**|[**GeoJSON Data Format**](system-requirements.md/#322-geojson-data-format)|Message|5.2|[WorkZoneFeed Schema](data-concepts.md/#52-workzonefeed-schema)|
| | |Message|5.5|[DeviceFeed Schema](data-concepts.md/#55-devicefeed-schema)|
|**3.2.3**|[**GeoJSON Data Validation**](system-requirements.md/#323-geojson-data-validation)|Message|5.2|[WorkZoneFeed Schema](data-concepts.md/#5311-publisher)|
| | |Message|5.5|[DeviceFeed Schema](data-concepts.md/#55-devicefeed-schema)|
|**3.2.4**|[**Business Rules**](system-requirements.md/#324-business-rules)|NA | | |
| | | | | |
|**3.3**|[**Data Exchange Requirements**](system-requirements.md/#33-data-exchange-requirements)| | | |
|**3.3.1**|[**Exchange WorkZoneFeed Information**](system-requirements.md/#331-exchange-workzonefeed-information)| | | |
|3.3.1.1|[Send WorkZoneFeed Information Upon Request](system-requirements.md/#3311-send-workzonefeed-upon-request)|Dialog|4.2|[Poll for Data Dialog](dialogs.md/#42-poll-for-data-dialog)|
|||Message|5.2|[WorkZoneFeed Schema](data-concepts.md/#52-workzonefeed-schema)|
|**3.3.2**|[**Exchange DeviceFeed Information**](system-requirements.md/#332-exchange-devicefeed-information)| | | |
|3.3.2.1|[Send DeviceFeed Information Upon Request](system-requirements.md/#3321-send-devicefeed-upon-request)|Dialog|4.2|[Poll for Data Dialog](dialogs.md/#42-poll-for-data-dialog)|
|||Message|5.5|[DeviceFeed Schema](data-concepts.md/#55-devicefeed-schema)|
||||||
|**3.4**|[**WorkZoneFeed Requirements**](system-requirements.md/#34-workzonefeed-requirements)|**Message**|**5.2**|[**WorkZoneFeed Schema**](data-concepts.md/#52-workzonefeed-schema)|
|**3.4.1**|[**Contents of WorkZoneFeed**](system-requirements.md/#341-contents-of-workzonefeed)|**Data Frame**|**5.2.1**|[**Properties**](data-concepts.md/#521-properties)|
|3.4.1 a)|[feed\_info](system-requirements.md/#341a)|Data Frame|5.2.1.1|[feed\_info](data-concepts.md/#5211-feed_info)|
|3.4.1 b)|[type](system-requirements.md/#341b)|Data Element|5.2.1.2|[type](data-concepts.md/#5212-type)|
|3.4.1 c)|[features](system-requirements.md/#341c)|Data Frame|5.2.1.3|[features](data-concepts.md/#5213-features)|
|3.4.1 d)|[bbox](system-requirements.md/#341d)|Data Frame|5.2.1.4|[bbox](data-concepts.md/#5214-bbox)|
||||||
|**3.5**|[**FeedInfo Requirements**](system-requirements.md/#35-feedinfo-requirements)| |**5.3**|[**FeedInfo Schema**](data-concepts.md/#53-feedinfo-schema)|
|**3.5.1**|[**Contents of FeedInfo**](system-requirements.md/#351-contents-of-feedinfo)|**Data Frame**|**5.3.1**|[**Properties**](data-concepts.md/#531-properties)|
|3.5.1 a)|[publisher](system-requirements.md/#351a)|Data Element|5.3.1.1|[publisher](data-concepts.md/#5311-publisher)|
|3.5.1 b)|[contact\_name](system-requirements.md/#351b)|Data Element|5.3.1.2|[contact\_name](data-concepts.md/#5312-contact_name)|
|3.5.1 c)|[contact\_email](system-requirements.md/#351c)|Data Element|5.3.1.3|[contact\_email](data-concepts.md/#5313-contact_email)|
|3.5.1 d)|[update\_frequency](system-requirements.md/#351d)|Data Element|5.3.1.4|[update\_frequency](data-concepts.md/#5314-update_frequency)|
|3.5.1 e)|[update\_date](system-requirements.md/#351e)|Data Element|5.3.1.5|[update\_date](data-concepts.md/#5315-update_date)|
|3.5.1 f)|[version](system-requirements.md/#351f)|Data Element|5.3.1.6|[version](data-concepts.md/#5316-version)|
|3.5.1 g)|[license](system-requirements.md/#351g)|Data Element|5.3.1.7|[license](data-concepts.md/#5317-license)|
|3.5.1 h)|[data\_sources](system-requirements.md/#351h)|Data Frame|5.3.1.8|[data\_sources](data-concepts.md/#5318-data_sources)|
|**3.5.2**|[**Contents of FeedDataSource**](system-requirements.md/#352-contents-of-feeddatasource)|**Data Frame**|**5.3.2.1**|[**FeedDataSource**](data-concepts.md/#5321-feeddatasource)|
|3.5.2 a)|[data\_source\_id](system-requirements.md/#352a)|Data Element|5.3.2.1.1|[data\_source\_id](data-concepts.md/#53211-data_source_id)|
|3.5.2 b)|[organization\_name](system-requirements.md/#352b)|Data Element|5.3.2.1.2|[organization\_name](data-concepts.md/#53212-organization_name)|
|3.5.2 c)|[contact\_name](system-requirements.md/#352c)|Data Element|5.3.2.1.3|[contact\_name](data-concepts.md/#53213-contact_name)|
|3.5.2 d)|[contact\_email](system-requirements.md/#352d)|Data Element|5.3.2.1.4|[contact\_email](data-concepts.md/#53214-contact_email)|
|3.5.2 e)|[update\_frequency](system-requirements.md/#352e)|Data Element|5.3.2.1.5|[update\_frequency](data-concepts.md/#53215-update_frequency)|
|3.5.2 f)|[update\_date](system-requirements.md/#352f)|Data Element|5.3.2.1.6|[update\_date](data-concepts.md/#53216-update_date)|
||||||
|**3.6**|[**RoadEventFeature Requirements**](system-requirements.md/#36-roadeventfeature-requirements)| |**5.4**|[**RoadEventFeature Schema**](data-concepts.md/#54-roadeventfeature-schema)|
|**3.6.1**|[**Contents of RoadEventFeature**](system-requirements.md/#361-contents-of-roadeventfeature)|**Data Frame**|**5.4.1**|[**Properties**](data-concepts.md/#541-properties)|
|3.6.1 a)|[id](system-requirements.md/#361a)|Data Element|5.4.1.1|[id](data-concepts.md/#5411-id)|
|3.6.1 b)|[type](system-requirements.md/#361b)|Data Element|5.4.1.2|[type](data-concepts.md/#5412-type)|
|3.6.1 c)|[properties](system-requirements.md/#361c)|Data Frame|5.4.1.3|[properties](data-concepts.md/#5413-properties)|
|3.6.1 d)|[geometry](system-requirements.md/#361d)|Data Frame|5.4.1.4|[geometry](data-concepts.md/#5414-geometry)|
|3.6.1 e)|[bbox](system-requirements.md/#361e)|Data Frame|5.4.1.5|[bbox](data-concepts.md/#5415-bbox)|
|**3.6.2**|[**Contents of WorkZoneRoadEvent**](system-requirements.md/#362-contents-of-workzoneroadevent)|**Data Frame**|**5.4.2.1**|[**WorkZoneRoadEvent**](data-concepts.md/#5421-workzoneroadevent)|
|3.6.2 a)|[core\_details](system-requirements.md/#362a)|Data Frame|5.4.2.1.1|[core\_details](data-concepts.md/#54211-core_details)|
|3.6.2 b)|[beginning\_cross\_street](system-requirements.md/#362b)|Data Element|5.4.2.1.2|[beginning\_cross\_street](data-concepts.md/#54212-beginning_cross_street)|
|3.6.2 c)|[ending\_cross\_street](system-requirements.md/#362c)|Data Element|5.4.2.1.3|[ending\_cross\_street](data-concepts.md/#54213-ending_cross_street)|
|3.6.2 d)|[beginning\_reference\_post](system-requirements.md/#362d)|Data Element|5.4.2.1.4|[beginning\_reference\_post](data-concepts.md/#54214-beginning_reference_post)|
|3.6.2 e)|[ending\_reference\_post](system-requirements.md/#362e)|Data Element|5.4.2.1.5|[ending\_reference\_post](data-concepts.md/#54215-ending_reference_post)|
|3.6.2 f)|[reference\_post\_unit](system-requirements.md/#362f)|Data Element|5.4.2.1.6|[reference\_post\_unit](data-concepts.md/#54216-reference_post_unit)|
|3.6.2 g)|[is\_start\_position\_verified](system-requirements.md/#362g)|Data Element|5.4.2.1.7|[is\_start\_position\_verified](data-concepts.md/#54217-is_start_position_verified)|
|3.6.2 h)|[is\_end\_position\_verified](system-requirements.md/#362h)|Data Element|5.4.2.1.8|[is\_end\_position\_verified](data-concepts.md/#54218-is_end_position_verified)|
|3.6.2 i)|[start\_date](system-requirements.md/#362i)|Data Element|5.4.2.1.9|[start\_date](data-concepts.md/#54219-start_date)|
|3.6.2 j)|[end\_date](system-requirements.md/#362j)|Data Element|5.4.2.1.10|[end\_date](data-concepts.md/#542110-end_date)|
|3.6.2 k)|[is\_start\_date\_verified](system-requirements.md/#362k)|Data Element|5.4.2.1.11|[is\_start\_date\_verified](data-concepts.md/#542111-is_start_date_verified)|
|3.6.2 l)|[is\_end\_date\_verified](system-requirements.md/#362l)|Data Element|5.4.2.1.12|[is\_end\_date\_verified](data-concepts.md/#542112-is_end_date_verified)|
|3.6.2 m)|[work\_zone\_type](system-requirements.md/#362m)|Data Element|5.4.2.1.13|[work\_zone\_type](data-concepts.md/#542113-work_zone_type)|
|3.6.2 n)|[vehicle\_impact](system-requirements.md/#362n)|Data Element|5.4.2.1.14|[vehicle\_impact](data-concepts.md/#542114-vehicle_impact)|
|3.6.2 o)|[location\_method](system-requirements.md/#362o)|Data Element|5.4.2.1.15|[location\_method](data-concepts.md/#542115-location_method)|
|3.6.2 p)|[worker\_presence](system-requirements.md/#362p)|Data Element|5.4.2.1.16|[worker\_presence](data-concepts.md/#542116-worker_presence)|
|3.6.2 q)|[reduced\_speed\_limit\_kph](system-requirements.md/#362q)|Data Element|5.4.2.1.17|[reduced\_speed\_limit\_kph](data-concepts.md/#542117-reduced_speed_limit_kph)|
|3.6.2 r)|[restrictions](system-requirements.md/#362r)|Data Frame|5.4.2.1.18|[restrictions](data-concepts.md/#542118-restrictions)|
|3.6.2 s)|[types\_of\_work](system-requirements.md/#362s)|Data Frame|5.4.2.1.19|[types\_of\_work](data-concepts.md/#542119-types_of_work)|
|3.6.2 t)|[lanes](system-requirements.md/#362t)|Data Frame|5.4.2.1.20|[lanes](data-concepts.md/#542120-lanes)|
|3.6.2 u)|[impacted\_cds\_curb\_zones](system-requirements.md/#362u)|Data Frame|5.4.2.1.21|[impacted\_cds\_curb\_zones](data-concepts.md/#542121-impacted_cds_curb_zones)|
|**3.6.3**|[**Contents of DetourRoadEvent**](system-requirements.md/#363-contents-of-detourroadevent)|**Data Frame**|**5.4.2.2**|[**DetourRoadEvent**](data-concepts.md/#5422-detourroadevent)|
|3.6.3 a)|[core\_details](system-requirements.md/#363a)|Data Frame|5.4.2.2.1|[core\_details](data-concepts.md/#54221-core_details)|
|3.6.3 b)|[beginning\_cross\_street](system-requirements.md/#363b)|Data Element|5.4.2.2.2|[beginning\_cross\_street](data-concepts.md/#54222-beginning_cross_street)|
|3.6.3 c)|[ending\_cross\_street](system-requirements.md/#363c)|Data Element|5.4.2.2.3|[ending\_cross\_street](data-concepts.md/#54223-ending_cross_street)|
|3.6.3 d)|[beginning\_reference\_post](system-requirements.md/#363d)|Data Element|5.4.2.2.4|[beginning\_reference\_post](data-concepts.md/#54224-beginning_reference_post)|
|3.6.3 e)|[ending\_reference\_post](system-requirements.md/#363e)|Data Element|5.4.2.2.5|[ending\_reference\_post](data-concepts.md/#54225-ending_reference_post)|
|3.6.3 f)|[reference\_post\_unit](system-requirements.md/#363f)|Data Element|5.4.2.2.6|[reference\_post\_unit](data-concepts.md/#54226-reference_post_unit)|
|3.6.3 g)|[start\_date](system-requirements.md/#363g)|Data Element|5.4.2.2.7|[start\_date](data-concepts.md/#54227-start_date)|
|3.6.3 h)|[end\_date](system-requirements.md/#363h)|Data Element|5.4.2.2.8|[end\_date](data-concepts.md/#54228-end_date)|
|3.6.3 i)|[is\_start\_date\_verified](system-requirements.md/#363i)|Data Element|5.4.2.2.9|[is\_start\_date\_verified](data-concepts.md/#54229-is_start_date_verified)|
|3.6.3 j)|[is\_end\_date\_verified](system-requirements.md/#363j)|Data Element|5.4.2.2.10|[is\_end\_date\_verified](data-concepts.md/#542210-is_end_date_verified)|
|**3.6.4**|[**Contents of RoadEventCoreDetails**](system-requirements.md/#364-contents-of-roadeventcoredetails)|**Data Frame**|**5.4.2.3**|[**RoadEventCoreDetails**](data-concepts.md/#5423-roadeventcoredetails)|
|3.6.4 a)|[data\_source\_id](system-requirements.md/#364a)|Data Element|5.4.2.3.1|[data\_source\_id](data-concepts.md/#54231-data_source_id)|
|3.6.4 b)|[event\_type](system-requirements.md/#364b)|Data Element|5.4.2.3.2|[event\_type](data-concepts.md/#54232-event_type)|
|3.6.4 c)|[related\_road\_events](system-requirements.md/#364c)|Data Frame|5.4.2.3.3|[related\_road\_events](data-concepts.md/#54233-related_road_events)|
|3.6.4 d)|[project\_id](system-requirements.md/#364d)|Data Frame|5.4.2.3.4|[project\_id](data-concepts.md/#54234-project_id)|
|3.6.4 e)|[road\_names](system-requirements.md/#364e)|Data Frame|5.4.2.3.5|[road\_names](data-concepts.md/#54235-road_names)|
|3.6.4 f)|[direction](system-requirements.md/#364f)|Data Element|5.4.2.3.6|[direction](data-concepts.md/#54236-direction)|
|3.6.4 g)|[name](system-requirements.md/#364g)|Data Element|5.4.2.3.7|[name](data-concepts.md/#54237-name)|
|3.6.4 h)|[description](system-requirements.md/#364h)|Data Element|5.4.2.3.8|[description](data-concepts.md/#54238-description)|
|3.6.4 i)|[creation\_date](system-requirements.md/#364i)|Data Element|5.4.2.3.9|[creation\_date](data-concepts.md/#54239-creation_date)|
|3.6.4 j)|[update\_date](system-requirements.md/#364j)|Data Element|5.4.2.3.10|[update\_date](data-concepts.md/#542310-update_date)|
|**3.6.5**|[**Enumeration of LocationMethod**](system-requirements.md/#365-enumeration-of-locationmethod)|**Data Element**|**5.4.2.4**|[**LocationMethod**](data-concepts.md/#5424-locationmethod)|
|**3.6.6**|[**Contents of RelatedRoadEvent**](system-requirements.md/#366-contents-of-relatedroadevent)|**Data Frame**|**5.4.2.5**|[**RelatedRoadEvent**](data-concepts.md/#5425-relatedroadevent)|
|3.6.6 a)|[type](system-requirements.md/#366a)|Data Element|5.4.2.5.1|[type](data-concepts.md/#54251-type)|
|3.6.6 b)|[id](system-requirements.md/#366b)|Data Element|5.4.2.5.2|[id](data-concepts.md/#54252-id)|
|**3.6.7**|[**Contents of TypeOfWork**](system-requirements.md/#367-contents-of-typeofwork)|**Data Frame**|**5.4.2.6**|[**TypeOfWork**](data-concepts.md/#5426-typeofwork)|
|3.6.7 a)|[type\_name](system-requirements.md/#367a)|Data Element|5.4.2.6.1|[type\_name](data-concepts.md/#54261-type_name)|
|3.6.7 b)|[is\_architectural\_change](system-requirements.md/#367b)|Data Element|5.4.2.6.2|[is\_architectural\_change](data-concepts.md/#54262-is_architectural_change)|
|**3.6.8**|[**Contents of Lane**](system-requirements.md/#368-contents-of-lane)|**Data Frame**|**5.4.2.7**|[**Lane**](data-concepts.md/#5427-lane)|
|3.6.8 a)|[order](system-requirements.md/#368a)|Data Element|5.4.2.7.1|[order](data-concepts.md/#54271-order)|
|3.6.8 b)|[status](system-requirements.md/#368b)|Data Element|5.4.2.7.2|[status](data-concepts.md/#54272-status)|
|3.6.8 c)|[type](system-requirements.md/#368c)|Data Element|5.4.2.7.3|[type](data-concepts.md/#54273-type)|
|3.6.8 d)|[restrictions](system-requirements.md/#368d)|Data Frame|5.4.2.7.4|[restrictions](data-concepts.md/#54274-restrictions)|
|**3.6.9**|[**Contents of Restriction**](system-requirements.md/#369-contents-of-restriction)|**Data Frame**|**5.4.2.8**|[**Restriction**](data-concepts.md/#5428-restriction)|
|3.6.9 a)|[type](system-requirements.md/#369a)|Data Element|5.4.2.8.1|[type](data-concepts.md/#54281-type)|
|3.6.9 b)|[value](system-requirements.md/#369b)|Data Element|5.4.2.8.2|[value](data-concepts.md/#54282-value)|
|3.6.9 c)|[[unit](system-requirements.md/#369c)|Data Element|5.4.2.8.3|[unit](data-concepts.md/#54283-unit)|
|**3.6.10**|[**Contents of CdsCurbZonesReference**](system-requirements.md/#3610-contents-of-cdscurbzonesreference)|**Data Frame**|**5.4.2.9**|[**CdsCurbZonesReference**](data-concepts.md/#5429-cdscurbzonesreference)|
|3.6.10 a)|[cds\_curb\_zone\_ids](system-requirements.md/#3610a)|Data Frame|5.4.2.9.1|[cds\_curb\_zone\_ids](data-concepts.md/#54291-cds_curb_zone_ids)|
|3.6.10 b)|[cds\_curbs\_api\_url](system-requirements.md/#3610b)|Data Element|5.4.2.9.2|[cds\_curbs\_api\_url](data-concepts.md/#54292-cds_curbs_api_url)|
|**3.6.11**|**Contents of WorkerPresence**|**Data Frame**|**5.4.2.10**|[**WorkerPresence**](data-concepts.md/#54210-workerpresence)|
|3.6.11 a)|[are\_workers\_present](system-requirements.md/#3611a)|Data Element|5.4.2.10.1|[are\_workers\_present](data-concepts.md/#542101-are_workers_present)|
|3.6.11 b)|[method](system-requirements.md/#3611b)|Data Element|5.4.2.10.2|[method](data-concepts.md/#542102-method)|
|3.6.11 c)|[worker\_presence\_last\_confirmed\_date](system-requirements.md/#3611c)|Data Element|5.4.2.10.3|[worker\_presence\_last\_confirmed\_date](data-concepts.md/#542103-worker_presence_last_confirmed_date)|
|3.6.11 d)|[confidence](system-requirements.md/#3611d)|Data Element|5.4.2.10.4|[confidence](data-concepts.md/#542104-confidence)|
|3.6.11 e)|[definition](system-requirements.md/#3611e)|Data Frame|5.4.2.10.5|[definition](data-concepts.md/#542105-definition)|
|3.6.11 f)|[other\_method](system-requirements.md/#3611f)|Data Element|5.4.2.10.6|[other\_method](data-concepts.md/#542106-other_method)|
|**3.6.12**|[**Enumeration of EventType**](system-requirements.md/#3612-enumeration-of-eventtype)|**Data Element**|**5.4.2.11**|[**EventType**](data-concepts.md/#54211-eventtype)|
|**3.6.13**|[**Enumeration of WorkZoneType**](system-requirements.md/#3613-enumeration-of-workzonetype)|**Data Element**|**5.4.2.12**|[**WorkZoneType**](data-concepts.md/#54212-workzonetype)|
|**3.6.14**|[**Enumeration of VehicleImpact**](system-requirements.md/#3614-enumeration-of-vehicleimpact)|**Data Element**|**5.4.2.13**|[**VehicleImpact**](data-concepts.md/#54213-vehicleimpact)|
|**3.6.15**|[**Enumeration of RestrictionType**](system-requirements.md/#3615-enumeration-of-restrictiontype)|**Data Element**|**5.4.2.14**|[**RestrictionType**](data-concepts.md/#54214-restrictiontype)|
|**3.6.16**|[**Enumeration of WorkTypeName**](system-requirements.md/#3616-enumeration-of-worktypename)|**Data Element**|**5.4.2.15**|[**WorkTypeName**](data-concepts.md/#54215-worktypename)|
|**3.6.17**|[**Enumeration of LaneStatus**](system-requirements.md/#3617-enumeration-of-lanestatus)|**Data Element**|**5.4.2.16**|[**LaneStatus**](data-concepts.md/#54216-lanestatus)|
|**3.6.18**|[**Enumeration of LaneType**](system-requirements.md/#3618-enumeration-of-lanetype)|**Data Element**|**5.4.2.17**|[**LaneType**](data-concepts.md/#54217-lanetype)|
|**3.6.19**|[**Enumeration of UnitOfMeasurement**](system-requirements.md/#3619-enumeration-of-unitofmeasurement)|**Data Element**|**5.4.2.18**|[**UnitOfMeasurement**](data-concepts.md/#54218-unitofmeasurement)|
|**3.6.20**|[**Enumeration of WorkerPresenceMethod**](system-requirements.md/#3620-enumeration-of-workerpresencemethod)|**Data Element**|**5.4.2.19**|[**WorkerPresenceMethod**](data-concepts.md/#54219-workerpresencemethod)|
|**3.6.21**|[**Enumeration of WorkerPresenceDefinition**](system-requirements.md/#3621-enumeration-of-workerpresencedefinition)|**Data Element**|**5.4.2.20**|[**WorkerPresenceDefinition**](data-concepts.md/#54220-workerpresencedefinition)|
|**3.6.22**|[**Enumeration of WorkerPresenceConfidence**](system-requirements.md/#3622-enumeration-of-workerpresenceconfidence)|**Data Element**|**5.4.2.21**|[**WorkerPresenceConfidence**](data-concepts.md/#54221-workerpresenceconfidence)|
|**3.6.23**|[**Enumeration of RelatedRoadEventType**](system-requirements.md/#3623-enumeration-of-relatedroadeventtype)|**Data Element**|**5.4.2.22**|[**RelatedRoadEventType**](data-concepts.md/#54222-relatedroadeventtype)|
||||||
|**3.7**|[**DeviceFeed Requirements**](system-requirements.md/#37-devicefeed-requirements)|**Message**|**5.5**|[**DeviceFeed Schema**](data-concepts.md/#55-devicefeedschema)|
|**3.7.1**|[**Contents of DeviceFeed**](system-requirements.md/#371-contents-of-devicefeed)|**Data Frame**|**5.5.1**|[**Properties**](data-concepts.md/#551-properties)|
|3.7.1 a)|[feed\_info](system-requirements.md/#371a)|Data Frame|5.5.1.1|[feed\_info](data-concepts.md/#5511-feed_info)|
|3.7.1 b)|[type](system-requirements.md/#371b)|Data Element|5.5.1.2|[type](data-concepts.md/#5512-type)|
|3.7.1 c)|[features](system-requirements.md/#371c)|Data Frame|5.5.1.3|[features](data-concepts.md/#5513-features)|
|3.7.1 d)|[bbox](system-requirements.md/#371d)|Data Frame|5.5.1.4|[bbox](data-concepts.md/#5514-bbox)|
|**3.7.2**|[**Contents of FieldDeviceFeature**](system-requirements.md/#372-contents-of-fielddevicefeature)|**Data Frame**|**5.5.2.1**|**FieldDeviceFeature**|
|3.7.2 a)|[id](system-requirements.md/#372a)|Data Element|5.5.2.1.1|[id](data-concepts.md/#55211-id)|
|3.7.2 b)|[type](system-requirements.md/#372b)|Data Element|5.5.2.1.2|[type](data-concepts.md/#55212-type)|
|3.7.2 c)|[properties](system-requirements.md/#372c)|Data Frame|5.5.2.1.3|[properties](data-concepts.md/#55213-properties)|
|3.7.2 d)|[geometry](system-requirements.md/#372d)|Data Frame|5.5.2.1.4|[geometry](data-concepts.md/#55214-geometry)|
|3.7.2 e)|[bbox](system-requirements.md/#372e)|Data Frame|5.5.2.1.5|[bbox](data-concepts.md/#55215-bbox)|
|**3.7.3**|[**Contents of FieldDeviceCoreDetails**](system-requirements.md/#373-contents-of-fielddevicecoredetails)|**Data Frame**|**5.5.2.2**|**FieldDeviceCoreDetails**|
|3.7.3 a)|[device\_type](system-requirements.md/#373a)|Data Element|5.5.2.2.1|[device\_type](data-concepts.md/#55221-device_type)|
|3.7.3 b)|[data\_source\_id](system-requirements.md/#373b)|Data Element|5.5.2.2.2|[data\_source\_id](data-concepts.md/#55222-data_source_id)|
|3.7.3 c)|[device\_status](system-requirements.md/#373c)|Data Element|5.5.2.2.3|[device\_status](data-concepts.md/#55223-device_status)|
|3.7.3 d)|[update\_date](system-requirements.md/#373d)|Data Element|5.5.2.2.4|[update\_date](data-concepts.md/#55224-update_date)|
|3.7.3 e)|[has\_automatic\_location](system-requirements.md/#373e)|Data Element|5.5.2.2.5|[has\_automatic\_location](data-concepts.md/#55225-has_automatic_location)|
|3.7.3 f)|[road\_direction](system-requirements.md/#373f)|Data Element|5.5.2.2.6|[road\_direction](data-concepts.md/#55226-road_direction)|
|3.7.3 g)|[road\_names](system-requirements.md/#373g)|Data Frame|5.5.2.2.7|[road\_names](data-concepts.md/#55227-road_names)|
|3.7.3 h)|[name](system-requirements.md/#373h)|Data Element|5.5.2.2.8|[name](data-concepts.md/#55228-name)|
|3.7.3 i)|[description](system-requirements.md/#373i)|Data Element|5.5.2.2.9|[description](data-concepts.md/#55229-description)|
|3.7.3 j)|[status\_messages](system-requirements.md/#373j)|Data Frame|5.5.2.2.10|[status\_message](data-concepts.md/#552210-status_messages)|
|3.7.3 k)|[is\_moving](system-requirements.md/#373k)|Data Element|5.5.2.2.11|[is\_moving](data-concepts.md/#552211-is_moving)|
|3.7.3 l)|[road\_event\_ids](system-requirements.md/#373l)|Data Frame|5.5.2.2.12|[road\_event\_ids](data-concepts.md/#552212-road_event_ids)|
|3.7.3 m)|[project\_id](system-requirements.md/#373m)|Data Element|5.5.2.2.13|[project\_id](data-concepts.md/#552213-project_id)|
|3.7.3 n)|[reference\_post](system-requirements.md/#373n)|Data Element|5.5.2.2.14|[reference\_post](data-concepts.md/#552214-reference_post)|
|3.7.3 o)|[reference\_post\_unit](system-requirements.md/#373o)|Data Element|5.5.2.2.15|[reference\_post\_unit](data-concepts.md/#552215-reference_post_unit)|
|3.7.3 p)|[make](system-requirements.md/#373p)|Data Element|5.5.2.2.16|[make](data-concepts.md/#552216-make)|
|3.7.3 q)|[model](system-requirements.md/#373q)|Data Element|5.5.2.2.17|[model](data-concepts.md/#552217-model)|
|3.7.3 r)|[serial\_number](system-requirements.md/#373r)|Data Element|5.5.2.2.18|[serial\_number](data-concepts.md/#552218-serial_number)|
|3.7.3 s)|[firmware\_version](system-requirements.md/#373s)|Data Element|5.5.2.2.19|[firmware\_version](data-concepts.md/#552219-firmware_version)|
|3.7.3 t)|[velocity\_kph](system-requirements.md/#373t)|Data Element|5.5.2.2.20|[velocity\_kph](data-concepts.md/#552220-velocity_kph)|
|3.7.3 u)|[is\_in\_transport\_position](system-requirements.md/#373u)|Data Element|5.5.2.2.21|[is\_in\_transport\_position](data-concepts.md/#552221-is_in_transport_position)|
|**3.7.4**|[**Contents of ArrowBoard**](system-requirements.md/#374-contents-of-arrowboard)|**Data Frame**|**5.5.2.3**|**ArrowBoard**|
|3.7.4 a)|[core\_details](system-requirements.md/#374a)|Data Frame|5.5.2.3.1|[core\_details](data-concepts.md/#55231-core_details)|
|3.7.4 b)|[pattern](system-requirements.md/#374b)|Data Element|5.5.2.3.2|[pattern](data-concepts.md/#55232-pattern)|
|**3.7.5**|[**Contents of Camera**](system-requirements.md/#375-contents-of-camera)|**Data Frame**|**5.5.2.4**|**Camera**|
|3.7.5 a)|[core\_details](system-requirements.md/#375a)|Data Frame|5.5.2.4.1|[core\_details](data-concepts.md/#55241-core_details)|
|3.7.5 b)|[image\_url](system-requirements.md/#375b)|Data Element|5.5.2.4.2|[image\_url](data-concepts.md/#55242-image_url)|
|3.7.5 c)|[is\_image\_url\_public](system-requirements.md/#375c)|Data Element|5.5.2.4.3|[is\_image\_url\_public](data-concepts.md/#55243-is_image_url_public)|
|3.7.5 d)|[image\_timestamp](system-requirements.md/#375d)|Data Element|5.5.2.4.4|[image\_timestamp](data-concepts.md/#55244-image_timestamp)|
|3.7.5 e)|[video\_url](system-requirements.md/#375e)|Data Element|5.5.2.4.5|[video\_url](data-concepts.md/#55245-video_url)|
|3.7.5 f)|[is\_video\_url\_public](system-requirements.md/#375f)|Data Element|5.5.2.4.6|[is\_video\_url\_public](data-concepts.md/#55246-is_video_url_public)|
|3.7.5 g)|[video\_update\_frequency](system-requirements.md/#375g)|Data Element|5.5.2.4.7|[video\_update\_frequency](data-concepts.md/#55247-video_update_frequency)|
|**3.7.6**|[**Contents of DynamicMessageSign**](system-requirements.md/#376-contents-of-dynamicmessagesign)|**Data Frame**|**5.5.2.5**|**DynamicMessageSign**|
|3.7.6 a)|[core\_details](system-requirements.md/#376a)|Data Frame|5.5.2.5.1|[core\_details](data-concepts.md/#55251-core_details)|
|3.7.6 b)|[message\_multi\_string](system-requirements.md/#376b)|Data Element|5.5.2.5.2|[message\_multi\_string](data-concepts.md/#55252-message_multi_string)|
|**3.7.7**|**Contents of FlashingBeacon**|**Data Frame**|**5.5.2.6**|**FlashingBeacon**|
|3.7.7 a)|[core\_details](system-requirements.md/#377a)|Data Frame|5.5.2.6.1|[core\_details](data-concepts.md/#55261-core_details)|
|3.7.7 b)|[function](system-requirements.md/#377b)|Data Element|5.5.2.6.2|[function](data-concepts.md/#55262-function)|
|3.7.7 c)|[is\_flashing](system-requirements.md/#377c)|Data Element|5.5.2.6.3|[is\_flashing](data-concepts.md/#55263-is_flashing)|
|3.7.7 d)|[sign\_text](system-requirements.md/#377d)|Data Element|5.5.2.6.4|[sign\_text](data-concepts.md/#55264-sign_text)|
|**3.7.8**|**Contents of HybridSign**|**Data Frame**|**5.5.2.7**|**HybridSign**|
|3.7.8 a)|[core\_details](system-requirements.md/#378a)|Data Frame|5.5.2.7.1|[core\_details](data-concepts.md/#55271-core_details)|
|3.7.8 b)|[dynamic\_message\_function](system-requirements.md/#378b)|Data Element|5.5.2.7.2|[dynamic\_message\_function](data-concepts.md/#55272-dynamic_message_function)|
|3.7.8 c)|[dynamic\_message\_text](system-requirements.md/#378c)|Data Element|5.5.2.7.3|[dynamic\_message\_text](data-concepts.md/#55273-dynamic_message_text)|
|3.7.8 d)|[static\_sign\_text](system-requirements.md/#378d)|Data Element|5.5.2.7.4|[static\_sign\_text](data-concepts.md/#55274-static_sign_text)|
|**3.7.9**|**Contents of LocationMarker**|**Data Frame**|**5.5.2.8**|**LocationMarker**|
|3.7.9 a)|[core\_details](system-requirements.md/#379a)|Data Frame|5.5.2.8.1|[core\_details](data-concepts.md/#55281-core_details)|
|3.7.9 b)|[marked\_locations](system-requirements.md/#379b)|Data Frame|5.5.2.8.2|[marked\_locations](data-concepts.md/#55282-marked_locations)|
|**3.7.10**|**Contents of MarkedLocation**|**Data Frame**|**5.5.2.9**|**MarkedLocation**|
|3.7.10 a)|[type](system-requirements.md/#3710a)|Data Element|5.5.2.9.1|[type](data-concepts.md/#55291-type)|
|3.7.10 b)|[road\_event\_id](system-requirements.md/#3710b)|Data Element|5.5.2.9.2|[road\_event\_id](data-concepts.md/#55292-road_event_id)|
|**3.7.11**|**Contents of TrafficSensor**|**Data Frame**|**5.5.2.10**|**TrafficSensor**|
|3.7.11 a)|[core\_details](system-requirements.md/#3711a)|Data Frame|5.5.2.10.1|[core\_details](data-concepts.md/#552101-core_details)|
|3.7.11 b)|[collection\_interval\_start\_date](system-requirements.md/#3711b)|Data Element|5.5.2.10.2|[collection\_interval\_start\_date](data-concepts.md/#552102-collection_interval_start_date)|
|3.7.11 c)|[collection\_interval\_end\_date](system-requirements.md/#3711c)|Data Element|5.5.2.10.3|[collection\_interval\_end\_date](data-concepts.md/#552103-collection_interval_end_date)|
|3.7.11 d)|[average\_speed\_kph](system-requirements.md/#3711d)|Data Element|5.5.2.10.4|[average\_speed\_kph](data-concepts.md/#552104-average_speed_kph)|
|3.7.11 e)|[volume\_vph](system-requirements.md/#3711e)|Data Element|5.5.2.10.5|[volume\_vph](data-concepts.md/#552105-volume_vph)|
|3.7.11 f)|[occupancy\_percent](system-requirements.md/#3711f)|Data Element|5.5.2.10.6|[occupancy\_percent](data-concepts.md/#552106-occupancy_percent)|
|3.7.11 g)|[lane\_data](system-requirements.md/#3711g)|Data Frame|5.5.2.10.8|[lane\_data](data-concepts.md/#552107-lane_data)|
|**3.7.12**|**Contents of TrafficSensorLaneData**|**Data Frame**|**5.5.2.11**|**TrafficSensorLaneData**|
|3.7.12 a)|[lane\_order](system-requirements.md/#3712a)|Data Element|5.5.2.11.1|[lane\_order](data-concepts.md/#552111-lane_order)|
|3.7.12 b)|[road\_event\_id](system-requirements.md/#3712b)|Data Element|5.5.2.11.2|[road\_event\_id](data-concepts.md/#552112-road_event_id)|
|3.7.12 c)|[average\_speed\_kph](system-requirements.md/#3712c)|Data Element|5.5.2.11.3|[average\_speed\_kph](data-concepts.md/#552113-average_speed_kph)|
|3.7.12 d)|[volume\_vph](system-requirements.md/#3712d)|Data Element|5.5.2.11.4|[volume\_vph](data-concepts.md/#552114-volume_vph)|
|3.7.12 e)|[occupancy\_percent](system-requirements.md/#3712e)|Data Element|5.5.2.11.5|[occupancy\_percent](data-concepts.md/#552115-occupancy_percent)|
|**3.7.13**|**Contents of TrafficSignal**|**Data Frame**|**5.5.2.12**|**TrafficSignal**|
|3.7.13 a)|[core\_details](system-requirements.md/#3713a)|Data Frame|5.5.2.12.1|[core\_details](data-concepts.md/#552121-core_details)|
|3.7.13 b)|[mode](system-requirements.md/#3713b)|Data Element|5.5.2.12.2|[mode](data-concepts.md/#552122-mode)|
|**3.7.14**|**Contents of RoadsideUnit**|**Data Frame**|**5.5.2.13**|**RoadsideUnit**|
|3.7.14 a)|[core\_details](system-requirements.md/#3714a)|Data Frame|5.5.2.13.1|[core\_details](data-concepts.md/#552131-core_details)|
|3.7.14 b)|[message\_types](system-requirements.md/#3714b)|Data Frame|5.5.2.13.2|[message\_types](data-concepts.md/#552132-message_types)|
|**3.7.15**|**Enumeration of UnitOfMeasurement**|**Data Element**|**5.5.2.14**|**UnitOfMeasurement**|
|**3.7.16**|**Enumeration of ArrowBoardPattern**|**Data Element**|**5.5.2.15**|**ArrowBoardPattern**|
|**3.7.17**|**Enumeration of FieldDeviceType**|**Data Element**|**5.5.2.16**|**FieldDeviceType**|
|**3.7.18**|**Enumeration of FieldDeviceStatus**|**Data Element**|**5.5.2.17**|**FieldDeviceStatus**|
|**3.7.19**|**Enumeration of FlashingBeaconFunction**|**Data Element**|**5.5.2.18**|**FlashingBeacon**|
|**3.7.20**|**Enumeration of HybridSignDynamicMessageFunction**|**Data Element**|**5.5.2.19**|**HybridSignDynamicMessageFunction**|
|**3.7.21**|**Enumeration of MarkedLocationType**|**Data Element**|**5.5.2.20**|**MarkedLocationType**|
|**3.7.22**|**Enumeration of TrafficSignalMode**|**Data Element**|**5.5.2.21**|**TrafficSignalMode**|
|**3.7.23**|**Enumeration of RoadsideUnitMessageTypes**|**Data Element**|**5.5.2.22**|**RoadsideUnitMessageTypes**|
||||||
|**3.8**|**Direction Requirements**| |**5.6**|**Direction Schema**|
|**3.8.1**|**Enumeration of Direction**|**Data Element**|**5.6**|**Direction Schema**|
| | | | | |
|**3.9**|**BoundingBox Requirements**| |**5.7**|**BoundingBox Schema**|
|**3.9.1**|**Contents of BoundingBox**|**Data Frame**|**5.7**|**BoundingBox Schema**|



