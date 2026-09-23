# **Annex E** 

# **User Requests [Informative]** 

This annex documents needs, requirements, and design details identified and considered by the CWZ Working Group or its task forces but not incorporated into this CWZ Implementation Guide and Standard. The rationale for excluding these elements is also provided. Thie items in this section may be revisited and considered for future editions of the CWZ Implementation Guide and Standard. 

## **E.1 User Requests – Needs** 

This sub-section identifies user needs that were identified and considered by the CWZ Working Group, but are not addressed by this CWZ Implementation Guide and Standard. 

## **E.1.1 Tutorial – Data Exchange Roles and Mechanisms** 

## **2.4.3.1 Polling for Updates – An Alternative to Polling** 

Polling, which allows a data consumer to periodically request all available data, is easy to understand. An alternative, known as _polling for updates,_ enables the data consume _r_ . to retrieve only data that has changed within a specific timeframe (e.g., the last 12 hours). 

The scenario below with Paula (the data provider) and Chris (the data consumer) illustrates how this approach allows Paula to make more efficient use of paper and enables Chris to pinpoint the specific timeframe relevant to his needs. 

One benefit of polling for updates is the result of smaller transmissions of data. 

One disadvantage of polling for updates is the risk that a data consumer may miss updates if the specified time in the past is incorrect. 

## **2.4.3.2 Change-driven Updates Described as an Interaction Between Humans** 

Change-driven updates work differently: Paula sends only the pages that have changed, and she sends them immediately when a change occurs. This mechanism ensures that Chris’s dataset remains current and synchronized with Paula's in real-time. . 

Imagine that all the work zone information can fit on a single page for simplicity. Chris provides Paula with a piece of paper for authentication, which also includes his address. Let's imagine that mail service between Paula and Chris is practically instantaneous. 

When Paula detects a change, she edits the page to reflect the update in her dataset (binder). She then sends updated page along with its page number to all data consumers, including Chris. This ensures both Paula's and Chris’s data sets (binders) are perfectly synchronized. For scenarios including multiple work zones, Paula would send updates for all that have changed, so Chris and other data consumers would receive multiple updated pages. 

One benefit of change-driven updates is the result in smaller transmissions of data. A secondary benefit is that change-driven data exchange architectures scale well, supporting a growing number of data consumers and providers. 

One disadvantage is that it requires data consumers to have confidence that they have received every change that has occurred. 

**Rationale:** CWZ WG Discussion. 

- Both the Polling for Update and Change-driven Update data exchange mechanisms offer advantages and disadvantages for deployers. However, these disadvantages do not exist 

with the current Polling mechanism of WZDx. Developing a satisfactory design to overcome the disadvantages is a complex issue with many design considerations. inconsequently, the CRZ WG decided to postpone a design for a future update of the CWZ Standard. Therefore, the materials leading to the design, including this tutorial, associated needs, operational scenario, and requirements have been relocated to this Annex for future consideration. 

## **E.1.2 Architectural Needs** 

## **2.5.1.1 Architectural Need - Software and Documentation Repository** 

CWZ deployers need open and public access to open-source software and documentation to foster experimentation and application of the CWZ standard. For example, since 2023, the WZDx open GitHub repository provides access for potential CWZ deployers to gain knowledge and experience in CWZ standards application. 

## **Rationale** : 

- As stated, this is a goal. 

- The requirements developed from this need would not be testable. 

## **2.5.1.2 Architectural Need – Compatibility with Existing and Emerging Standards** 

CWZ deployers may need to use multiple standards (e.g., J2945/4 RSM, TMDD, J2735 TIM & RSM, and WZDx). To the extent practical, the CWZ Standard will strive to provide consistent data definitions and enumerations to facilitate the necessary conversions when moving data between formats governed by different standards. Where there is no consistency, the working group will provide guidance, such as a mapping table to translate from one standard to another. 

## **Rationale** : 

- The requirements developed from this need would not be testable. 

- As stated, this need is a goal. 

## **2.5.1.2.2 GeoJSON Data Exchange – Poll for Data Updates** 

CWZ deployers need to share work zone information updates only, given a point in time in the past, where work zone information is provided in the GeoJSON data format. Poll for Data Updates is a synchronous method of communication. 

## **2.5.1.2.3 GeoJSON Data Exchange – Change-driven Updates** 

CWZ data providers need the capability to asynchronously share updates only when changes occur. 

**Rationale:** CWZ WG Discussion. 

- The Polling for Update and Change-driven Update data exchange mechanisms have advantages and disadvantages for deployers. These disadvantages do not exist with the current Polling mechanism of WZDx. Developing a satisfactory design to overcome the disadvantages is a complex issue with many design considerations. It was the opinion of many in the WG to postpone a design for a future update of the CWZ Standard. Therefore, the materials leading to the design, including this tutorial, associated needs, and requirements have been relocated to this Annex for future consideration. 

## **2.5.1.3 Architectural Need – Extensible Framework** 

This CWZ standardization effort will largely be based on what can be practically and currently collected from and by IOOs. The capabilities and data collection practices of IOOs will likely develop over time to reflect new practices. Therefore: 

- CWZ deployers need a CWZ standard that will provide a consistent framework for data exchanges deployable today, while able to accommodate new needs that may arise over time. 

- CWZ deployers need a CWZ standard that will extend to new areas and categories of disruptions. 

- CWZ deployers need a CWZ standard that will extend to new areas and categories of VRUs. 

## **Rationale:** 

- The requirements from this need overlap with the need for backward compatibility. Backward compatibility provides an extensible framework, as defined above. 

- As stated, most of the content in this need is a goal. 

## **2.5.1.5 Architectural Need – Time Source** 

Currently, devices use varying methods and time sources to determine time (for example, to generate a timestamp); some devices use the Network Time Protocol (NTP), while others depend on the time provided by a Global Navigation Satellite System (GNSS) receiver. 

CWZ deployers need to maintain consistent time across various devices used in connected work zones. 

## **Rationale:** 

- No requirements nor design were identified for this need by the CWZ WG. 

## **2.5.1.6.2 Support Smaller, Condensed Packets of Information** 

The current JSON REST API provides all work zone activity for a particular data provider. That transferred information, when saved, results in a GeoJSON file that can be viewed with off-the-shelf software, such as a GIS. One drawback of this approach is that large datasets will likely not support the following: 

- “over the air” interfaces 

- the transfer of real-time or near real-time information. 

CWZ deployers need to support the exchange of smaller, condensed packets of information. 

CWZ deployers need to support a mechanism for data exchanges as follows: 

- Based on the exchange of smaller packets of information; 

- Supports updates for specific work zone information or subsets/fragments of work zone data (e.g., VRU locations, work vehicle, devices) without requiring the retransmission of static information that has not changed; 

- Supports exchanges where the data provider initiates the transfer of information. This contrasts with the current JSON REST API, which relies on polling initiated by the data consumer. 

## **Rationale: CWZ WG Discussion.** 

- Proposed to remove these texts. 

- There was agreement to remove. 

- The focus (scope) of this standard is center to center (Work Zone Center to External Center). 

- The WZDx and this ConOps should not cover Work Zone Devices to Work Zone Center. 

- General agreement. 

- The scope does not include polling or control of devices from Work Zone Center. 

- It was agreed to keep the change-driven discussion, which is included in another need. 

## **2.5.1.6.3 Support Confirmation Receipts** 

CWZ deployers need data exchanges to contain a confirmation receipt that verifies delivery when a data provider sends data to a data consumer. 

**Rationale:** CWZ WG Discussion. 

- Objective is to account for both delivery and confirmation of interpretation of the data. 

- Want acknowledgement that all data items in the “transaction” were read successfully. This is important for security and liability reasons. 

- Providers need a “key code” that authorizes the end-user's use of the data. This may be used as a confirmation that the end-user agrees to comply with an agreement. 

- It was agreed that this is a big topic and should be moved to the parking lot. 

## **2.5.1.9 Architectural Need – Goal / Mandatory and Optional Elements** 

CWZ deployers have the following concerns about mandatory and optional elements: 

- Optional items in the CWZ standard makes designs incompatible; 

- Optional data elements greatly affect the desired outcome of a common data structure to handle the content of work zone information; 

- Stakeholders involved in standards development tend to make data elements optional when: 

   - They cannot reach consensus agreement, or 

   - They anticipate that they will not be able to provide the data specified by the standard. 

CWZ deployers need greater consensus agreement on what is essential (i.e., mandatory). 

CWZ deployers need to handle mandatory elements when data is not available so they can use a common data structure, even if the data is not available. 

**Rationale:** CWZ WG Discussion. 

- Agreed that this is a challenge, but untestable, and there is not a process to support this goal. 

- There is not much that can be done about this, and therefore should be removed from the standard. 

## **2.5.1.10 Architectural Need – Goal / Machine Interpretable Data** 

CWZ deployers have systems that rely on data that does not require human interpretation, such as freeform fields. 

CWZ deployers need data as specified in the standard to be interpretable by machines. 

**Rationale** : 

- As stated, this is a goal. 

- The requirements developed from this need would not be testable. 

## **2.5.1.11 Architectural Need – Goal / Data Structure** 

CWZ deployers have the following architectural design goals: 

- Limit the use of 'choice' elements in the data structure that can enable multiple, if not infinite permutations of data structures, and non-interoperable designs, ambiguous interpretations of the data, and create errors in data interpretation. 

- A flat data structure is better than a deeply-nested structure. The current data structure is tending toward becoming heavily nested. Moving forward, the CWZ Working Group should consider more favorable designs with a flatter structure. 

- Enable an API to allow gathering of specific data for a CWZ. 

CWZ deployers need a single, consistent data structure that handles multiple situations, across actor components, and designs. 

**Rationale:** CWZ WG Discussion. 

- The assertions are unproven and requirements developed from this need would not be testable. 

- There is not much that can be done about this, and there is much engineering judgement involved. 

- This should be removed from the standard. 

## **2.5.1.12 Architectural Need – Zone Data Quality and Validation** 

## **2.5.1.12.1.1 Criteria for a Defined Quality of Information** 

CWZ deployers need criteria for evaluating the quality of work zone data. 

## **2.5.1.12.1.2 Support Information to Support Decision-making for Operations** 

CWZ data consumers need ~~accurate and correct~~ information to support decision-making for operations. 

## **2.5.1.12.1.3 Support Accurate and Correct Information to Facilitate Trip Planning** 

CWZ data consumers need ~~accurate and correct~~ information to support pre-trip route, and en-route trip planning. 

**Rationale:** CWZ WG Discussion. 

- If these are needs, will there be requirements and design to trace back to these needs? These items are not testable. 

- If we use the term accurate, we need to specify how accurate. 

- Equipment manufacturers do not typically provide information that is “interpreted.” 

## **2.5.1.12.2 Architectural Need – Zone Data Quality – Position/Geometry Is Correct** 

CWZ providers need to provide ~~correct and accurate~~ (the best the provider has available) zone geometry information when providing work zone information to data consumers. 

**Rationale:** CWZ WG Discussion. 

- If we use the term accurate, we need to specify how accurate. 

- Some feed providers can only provide a single point. 

- Define the source. 

- As defined above, quality is untestable. 

## **2.5.1.12.3 Architectural Need – Zone Data Quality – Time Work Zone is Active Is Correct** 

CWZ providers need to provide ~~correct and accurate zone~~ active time information when providing work zone information to data consumers. 

**Rationale:** As amended, this is a duplicate need. 

## **2.5.1.13 Architectural Need – Security-Trust** 

## **2.5.1.13.1 Support Cyber Security** 

CWZ deployers need cybersecurity to be a vital element of the CWZ Standard architecture. 

## **2.5.1.13.2 Verify Trusted Source of Information** 

CWZ deployers exchanging data need to verify whether a data provider is a trustworthy source. For example, one mechanism suggested by CWZ deployers is verification of a trusted source using security certificates and signing of data. 

## **2.5.1.13.3 Verify Authentication for Access** 

CWZ data providers need a mechanism for authorizing  data consumers. For example, one mechanism suggested by CWZ deployers is that API keys are used in conjunction with the JSON REST API. 

## **2.5.1.13.4 Support SCMS for Connected Vehicle Environment Deployments** 

CWZ deployers working in Connected Vehicle Environments need to access the SCMS for security services. 

**Rationale:** These security needs were identified as an operational constraint and highly dependent on each agency's security policies, which are not subject to this standard. 

## **2.5.1.15 Architectural Need – Feed Discovery** 

Potential CWZ data consumers need to know where to acquire work zone data being made available by data providers. 

**Rationale:** This need, the need for a mechanism and supporting systems to enable feed discovery, is outside the scope of this system interface standard. 

## **2.5.1.16 Architectural Need – Data Hub** 

CWZ deployers need a mechanism to allow aggregation of data from multiple or many data providers. 

**Rationale:** This data hub need is outside the scope of this system interface standard, as we are not writing requirements for a data hub. 

## **E.1.2.1 Architectural Needs – User Comment Draft Comments Received** 

The following comments were received during the User Comment Draft review. 

- In certain implementations of a Data Consumer / Data Provider polling system, the Data Provider may need to limit the quantity of data provided in order to allow the Data Provider to ensure internal systems are not effectively shut down due to overloaded throughput (i.e., effectively a Denial-of-Service attack). Some Data Providers may have policies to mitigate potential Denial of Service failures on their internal systems. As is written, the CWZ Standard implies that all available work zone data will be provided by a Data Provider upon request from a Data Consumer via the Poll communication system. However, depending on the frequency at which a Data Consumer issues a Poll Request and/or the total quantity of available data, it may be overly burdensome to a Data Provider to respond with all of the available data to each request. A Best Practice method of handling this type of scenario is with an implementation of data pagination, whereby a segment of the total available data is provided to the Data Consumer along with a method for the Data Consumer to subsequently issue a new request for the next segment, continued until the Data Consumer eventually requests all available data segments. Such a mechanism allows a Data Provider to ensure that internal systems are provisioned to support a maximum quantity of data analysis, preparation, and transfer based upon the quantity of Data Consumers making Poll requests and the total quantity of available data. 

- The ngTMDD has a new architectural need to support change-driven updates or event-driven updates. Designs developed by the ngTMDD may support the CWZ effort. 

**Rationale:** At this time, the ngTMDD design is underway, and it is unclear what direction the ngTMDD is going to take with respect to handling of Change-driven Updates. Furthermore, it is unclear when the design effort will include handling of Change-driven Updates. 

- Currently, the ngTMDD is planning an update to the TMDD location referencing scheme (node, link, route) to support lane-level granularity for new objects such as "link lane status" that can share the status (i.e., open, closed, or restricted) of specific lanes on an approach to a work zone. With respect to developing applications that could inform motorists which lanes are closed as they 

approach a work zone or other event, harmonization between CWZ (Section 3.6.17 Enumeration of LaneStatus) and ngTMDD lane status data concepts and objects would be beneficial. 

**Rationale:** At this time, the ngTMDD design is underway, and it is unclear what direction the ngTMDD is going to take with respect to roadway and general geographic referencing. Furthermore, it is unclear whether the ngTMDD design will be compatible with the GeoJSON approach used in CWZ. 

## **E.1.3 Data Exchange Needs** 

## **2.5.2.1.2 Zone Metadata – Zone Data Acknowledge Receipt** 

CWZ consumers need to provide a confirmation receipt as a proof of delivery of work zone data upon receipt of data from a CWZ data provider. 

**Rationale:** CWZ WG Discussion. 

- This is a receipt from the data consumer that the feed file was successfully read with no errors. 

- This would be optional, depending on the consumer. 

- This could be built on top of the API mechanism. 

- It was agreed that this is a big topic and should be moved to the parking lot. There is an accompanying need. 

## **2.5.2.1.5 Zone Metadata – GNSS Position Accuracy in Meters** 

CWZ data providers need to provide the locational accuracy or method of location information acquisition to determine the accuracy of geographic information, in meters, when providing work zone information to data consumers. 

A brief summary about the locational accuracy of work zone data collection methods is described below: 

- IOOs typically use standard GNSS, which provides 5- to 7-meter accuracy. 

- OEMs require high fidelity location data for lane determination. OEMs and navigation companies have digital maps with accuracies of approximately 10 centimeters. OEMs and navigation companies use LIDAR as measurement devices. OEMs state that this level of accuracy should not and does not have to be passed on to the IOOs. 

- The accuracy of current GNSS on-board OEM vehicles (which relies on multiple GNSS devices on-board the vehicle) in open environments is about 2 meters. Therefore, vehicles cannot determine which lane they are in. 

- Typical, standard GNSS cannot be used to acquire lane level detail of work zones. Therefore, creating lane-level geometry that depends on GNSS is unnecessary. 

- Device manufacturers have stated that an arrow board will provide 2-meter accuracy. 

**Rationale:** CWZ WG Discussion. 

- It is not the intent of the standard to define a required level of accuracy for position data, which varies greatly. 

- Most data providers cannot provide this right now. 

## **2.5.2.1.6 Zone Metadata – Zone Data Expiration End Date-Time** 

CWZ data providers need to provide zone data expiration date-time when providing work zone information to data consumers. Data consumers need to know the timeframe for which data is accurate and reliable, for example, to support decision-making. 

**Rationale:** CWZ WG Discussion. 

- No expiration date on DeviceFeed. 

- It is better to use end_date for the WorkZoneFeed. 

- Consensus is to remove this need. 

## **2.5.2.2.2 Zone Alerts and Notifications – VRU Position/Geometry** 

CWZ deployers want to notify/alert drivers when their vehicle is approaching a VRU's location. CWZ deployers may provide wearable devices to VRUs that can be used to locate a VRU within a CWZ. Vehicles warn their driver upon approach to the CWZ. 

CWZ data providers need to provide VRU position/geometry when providing work zone information to data consumers. 

**Rationale:** CWZ WG Discussion. 

- There are no alerts and notifications. 

- This is a redundant need. 

- Remove. 

## **2.5.2.2.3 Zone Alerts and Notifications – Zone Status, Speed Limits, and Lane Shifts** 

CWZ deployers use devices that automatically share status information to navigation companies. Typical information sent includes start of work zone, end of work zone, reduced speed limit zones, lane changes/shifts (and connections with arrow boards), and lane closures. Alerts show up in the navigation company's mobile applications or in OEMs' driver alert gadget. 

CWZ data providers need to provide zone status, speed limit zones, speed limits, lane shifts, lane tapers, and direction of lane shift, number of lanes to taper, and lane closures when providing work zone information to data consumers. 

**Rationale:** CWZ WG Discussion. 

- There are no alerts and notifications. 

- This is a redundant need. 

- Remove. 

## **2.5.2.2.4 Zone Alerts and Notifications – Intrusion Detection Geometry** 

CWZ deployers need work zone information to detect intrusions by vehicles into specific areas within the work zone. For example, areas where workers are present. 

CWZ data providers need to provide notification alerts to drivers, VRUs, and work zone centers when intrusions are detected. 

**Rationale:** CWZ WG Discussion. 

- There are no alerts and notifications. 

- This was determined to be out of scope. 

- Keep for future consideration. 

## **2.5.2.4.3 Zone Traffic – Crash Counts** 

## **2.5.2.4.3.1 Traffic Incident Management Performance Measures** 

CWZ deployers need to calculate incident durations related to crashes in a work zone consistent with the NOCOE Traffic Incident Management Performance Measures (TIM-PM) and Incident Timeline to assess the safety of work zone deployments. 

## **2.5.2.4.3.2 Traffic Incident Type and Location** 

CWZ data providers need to provide crash information such as type and location when providing work zone information to work zone data consumers. 

## **2.5.2.4.3.3 Crash Counts** 

CWZ data providers need to provide crash counts over a period of time when providing work zone information to work zone data consumers. 

**Rationale:** CWZ WG Discussion. 

- Data may come from: 

   - Attenuators have crash counts. 

   - Extract from CAN-bus data. 

   - First responder records. 

- Put in parking lot. There are different ways to get this information. 

## **2.5.2.2.5 Zone Alerts and Notifications – Zone Identifier** 

CWZ data providers need to provide the zone identifier associated with zone alerts and notifications when providing work zone information to work zone data consumers. 

## **2.5.2.3.6 Zone Status – Zone Identifier** 

CWZ data providers need to provide the zone identifier associated with zone status information when providing work zone information to work zone data consumers. 

## **2.5.2.4.4 Zone Traffic – Zone Identifier** 

CWZ data providers need to provide the zone identifier associated with zone traffic information when providing work zone information to work zone data consumers. 

## **2.5.2.5.6 Zone Lanes – Zone Identifier** 

CWZ data providers need to provide the zone identifier associated with zone lane information when providing work zone information to work zone data consumers. 

## **2.5.2.6.3 Zone VRU – Zone Identifier** 

CWZ data providers need to provide the zone identifier associated with a VRU when providing work zone information to work zone data consumers. 

## **2.5.2.7.3 Zone Work Vehicle – Zone Identifier** 

CWZ data providers need to provide the zone identifier associated with the work vehicle when providing work zone information to work zone data consumers. 

## **2.5.2.9.2 Zone Schedule – Zone Identifier** 

CWZ data providers need to provide the zone identifier associated with the zone schedule information when providing work zone information to work zone data consumers. 

## **2.5.2.10.3 Zone Speed Limit – Zone Identifier** 

CWZ data providers need to provide the zone identifier associated with the speed limit change information when providing work zone information to work zone data consumers. 

**Rationale:** CWZ WG Discussion. 

- Zone Identifiers are only needed for Devices to identify which zone the device is associated with. 

   - VRU is covered under Device. 

   - Work Vehicle is covered under Device. 

- There is no need to identify zone identifiers for these attributes of work zones. 

- Remove these identifiers. 

- Separate need was identified to identify travel time through the zone, for example by blue-tooth devices. 

## **E.1.4 Operational Scenarios** 

## **<u>VRU Safety</u> –** **<u>Zone Intrusion Detection and Notification Alerts (OUT OF SCOPE)</u>** 

|Title|VRU Safety–Zone Intrusion Detection|
|---|---|
|Problem<br>Aspect|A work zone may want a defined area to detect vehicle intrusions for VRU safety.|
|Description|Work zone equipment may be set up to detect vehicle intrusions into the work zone to<br>provide VRUs with enough warning to get to a safe location. Detection equipment may<br>include sensors, and alerting equipment may include flashing beacons, VRU electronic<br>safety vests, or personal devices (smartphone).|
|Pre-<br>Conditions|<br>The area being monitored for vehicle intrusion is defined.<br><br>Work zone device(s) monitoring this defined area is/are set up.<br><br>The work zone device(s) is/are connected to the work zone center.<br><br>(optional) The work zone devices are connected to each other.<br><br>VRUs in the area are wearing smart vests or carry a personal device connected to<br>the alerting equipment.<br><br>A work zone device detects an intrusion.|
|Optional<br>Diagram||
|Narrative and<br>Sequence of<br>Steps|1a) The work zone device sends an intrusion alert to the work zone VRU.<br>1b) The work zone device sends the intrusion information to the work zone center.<br>1c) (optional) The work zone device sends the intrusion information to other work<br>zone device(s) such as a flashing beacon.<br>2) (optional) The work zone center sends the intrusion information to other work<br>zone device(s).|
|End<br>Conditions or<br>State|VRUs are alerted of the intrusion with enough time to get to safety (through an<br>audio/haptic/visual alert on their vest or personal device and/or flashing beacons), and<br>the work zone center receives information about the intrusion.|
|Scenario<br>Extension|This may apply to other VRUs with a smartphone application.|



**Rationale:** CWZ WG Discussion. 

 This scenario is out of scope of this standard and should be removed. 



<!-- Start of picture text -->
WZ Data Collection  – From Devices (OUT OF SCOPE)<br>Title WZ Data Collection – From Devices<br>Problem  A work zone center needs to collect information gathered by work zone devices.<br>Aspect<br>Description A connected work zone may require the use of devices that gather data such as GPS<br>location or vehicle speeds. These devices may be directly connected to the work zone<br>center for maximum utility. A device may be work zone equipment such as a camera or<br>traffic sensor.<br>Pre- The work zone device is powered on and configured.<br>Conditions The work zone device is connected to the work zone center.<br>Optional<br>Diagram<br>Work Zone  1 Work Zone<br>Device Center<br>Narrative  The work zone device sends information to the work zone center continuously,<br>and  periodically, or as relevant events happen.<br>Sequence of<br>Steps<br>End  The work zone center receives the data collected by the work zone device.<br>Conditions<br>or State<br>Scenario  This may also apply to work zone vehicles and VRUs.<br>Extensions<br><!-- End of picture text -->

**Rationale:** CWZ WG Discussion. 

 This scenario is out of scope of this standard and should be removed. 

## **<u>2.6.6 Generic Work Zone Information Data Exchange (Change-driven Updates)</u>** 



<!-- Start of picture text -->
Title Generic Work Zone Data Exchange (Change-driven Updates)<br>Problem  A data consumer has a prior data set of work zone information that needs to be<br>Aspect updated. A data provider needs to send only information updates to allow the data<br>consumer's data set to be current.<br>Description When a data provider has new information, possibly due to an event, the data provider<br>needs to update a data consumer with information to bring the data consumer's data<br>set up-to-date. This may be a work zone needing to update a data consumer about a<br>new vehicle or VRU position, or changes in speed limits within a zone.<br>Pre-  The data consumer is an authorized connection to the data provider.<br>Conditions  The data provider has new information that needs to be communicated to a data<br>consumer.<br>Optional<br>Diagram<br>Data  1 Data<br>Provider Consumer<br>Narrative  1) The data provider sends updated information to the data consumer.<br>and<br>Sequence of<br>Steps<br>End  The data consumer has up-to-date information about work zones and conditions.<br>Conditions<br>or State<br><!-- End of picture text -->

**Rationale:** CWZ WG Discussion. 

- The Polling for Update and Change-driven update data exchange mechanisms have advantages and disadvantages for deployers. These disadvantages do not exist with the current Polling mechanism of WZDx. Developing a satisfactory design to overcome the disadvantages is a complex issue with many design considerations. It was the opinion of many in the WG to postpone a design for a future update of the CWZ Standard. Therefore, the materials leading to the design, including this tutorial, associated needs, operational scenarios, and requirements have been relocated to this Annex for future consideration. 

## **E.1.5 Relationship to ARC-IT** 

## **ARC-IT Work Zone Safety Monitoring Service Package [2.8.2] (OUT OF SCOPE)** 

<u>MC07: Work Zone Safety Monitoring. This service package provides warnings to maintenance personnel</u> within a work zone about potential hazards within the work zone. It enables vehicles or the infrastructure to provide warnings to workers in a work zone when a vehicle is moving in a manner that appears to create an unsafe condition (e.g., moving at high speed or entering the work zone). 



<!-- Start of picture text -->
(2C) work zone warning device control<br>(2C) work zone warning status<br>Maint and Constr ITS Roadway river information. driver information<br>Management Center| (28)workzonetraffic detectorwarning Gevcecontrol Equipment ‘OtherMCV OBES:<br>control (2A) traffic detector control + 2A) work:<br>4, 20) atte detector cata, video survellance control (2A) workzone<br>‘work zone warning status q 2A)wratfcmagetraffictratedetectormages mete  data+ deta + warning ncafieaion<br>cM Work Zone Roadway workzone Jie-—2229°2 Taintand Const | Personne<br>(28) work zone caus‘stationtrafic arg personnellupdates wongwazone| VehicleinandtatanOBE<br>ai wee) |i2a) workzone warning ;<br>application |notification Personnel Device<br>status (28) personnel_ |<br>(28) work 2Assf warming14) coonprsonnel_fet 118safetyTeton personne warning © I] sevwontorirg vente safety<br>wot Leer IF sonnel Work Zone<br>‘applicationine i Safety<br>|,L oadsieGemected EquipmentVehicle (2a)caton vehicle| | sgnage 24) vehicle<br>(2A) work zone warning notification anemotion data<br>(2A) veil catioa d n  mation ——<br>SE Work Zone sa<br>(a seat Treo azo [var]<br><!-- End of picture text -->

## **ARC-IT – Work Zone Safety Service Package Diagram [Figure 6].** 

**Rationale:** CWZ WG Discussion. 

- This portion of ARC-IT is out of scope of this standard and should be removed. 

## **E.2 User Requests – Requirements** 

This sub-section identifies requirements that were identified and considered by the CWZ Working Group but are not addressed in this CWZ Implementation Guide and Standard. 

## **3.3.1.2 Send WorkZoneFeed Upon Request for Updates** 

A data provider shall send WorkZoneFeed information upon request for updates from a data consumer. 

## **3.3.1.3 Send WorkZoneFeed Information Updates Upon Change of Information** 

A data provider shall send WorkZoneFeed updates to data consumers upon change in information. 

## **3.3.2.2 Send DeviceFeed Upon Request for Updates** 

A data provider shall send DeviceFeed information upon request for updates from a data consumer. 

## **3.3.2.3 Send DeviceFeed Information Updates Upon Change of Information** 

A data provider shall send DeviceFeed updates to data consumers upon change in information. 

**Rationale:** CWZ WG Discussion. 

- The Polling for Update and Change-driven update data exchange mechanisms have advantages and disadvantages for deployers. These disadvantages do not exist with the current Polling mechanism of WZDx. Developing a satisfactory design to overcome the disadvantages is a complex issue with many design considerations. It was the opinion of many in the WG to postpone a design for a future update of the CWZ Standard. Therefore, the materials leading to the design, including this tutorial, associated needs, 

operational scenarios, and requirements have been relocated to this Annex for future consideration. 

## **E.3 User Requests – Design Details** 

This sub-section identifies design details that were identified and considered by the CWZ Working Group, but are not addressed in this CWZ Implementation Guide and Standard. 

## **E.4 User Requests – Guidance Needs** 

This sub-section identifies guidance needs that were identified and considered by the CWZ Working Group, but are not addressed in this CWZ Implementation Guide and Standard. 

## **Guidance Needs - Contracting, Data Ownership, and Licensing [B.2]** 

CWZ deployers need guidance on how to develop contractor specs. For example, uptime requirements for contractors and penalties for downtime. Several IOOs are developing guidelines for testing connected work zone equipment; for example, equipment needs to pass a X-days of field test prior to using the device in an active work zone. These same IOOs, however, state that they are aware that some contractors will choose not to bid on the project due to the new testing requirements. 

## **Guidance Needs – Roadway Construction Contractor Scopes do not Require the Provision of Electronic Work Zone Information and Status [B.2.1]** 

Device manufacturers work with IOOs and contractors to deploy electronic equipment to serve a host of needs, including safety applications, guidance for drivers to maneuver passage through a work zone, etc. 

Contractors are not required by IOOs to deploy electronic field devices in work zones. Currently, the burden of communicating the benefits of connected work zones has traditionally fallen on the work zone device manufacturers, who are motivated to sell their equipment, and by some IOOs. Today, however, and moving forward, IOOs will need to take a larger role in communicating the benefits of CWZs within their own organizations, but also to assist with communicating the benefits to their contractors that ultimately will become responsible for the day-to-day operation of connected work zones. 

A few examples of the type of things that need to be stated in contract specs are the following: 

- the types of work zone equipment that needs to be planned, designed, engineered, and monitored 

- specifications so equipment is deployed correctly, accurately, and reliably 

- that workers need to use equipment to enable detection of worker presence and location within a work zone – workers may have wearable devices 

- where to positions location markers within the work zone 

- for connected vehicle deployments, the details of configuration of RSUs 

Contractor equipment need to be supported and tested to conform with standards for data communications. In addition, contractors may need to do data entry, keeping data available and up-todate, based on real-time requirements. 

Along with specifying contractual requirements, IOOs will need to enforce contractual requirements. 

## **Guidance Needs – Data Ownership and Licensing [B.2.2]** 

The topics of data ownership and licensing are closely related, and discussed briefly, below. 

## **Guidance Needs – Data Ownership [B.2.2.1]** 

In today's technology and data-driven environment, data is an asset and a source of intellectual property (IP) for data owners. Data owners add value to raw data through first acquiring the data, and then becoming responsible for maintenance, reliability, uptime, frequency of updates, and other quality factors. 

Data owners seek to monetize their data IP and can optimize and recoup their investment in value-added features, by limiting the usage and redistribution right of the data. 

Data ownership may also apply when addressing the source of the data, i.e., the equipment used that generates the data. For example, contractors may feel that they are the owners of data, since the data is generated and collected from their vehicles, devices they own, and workers they employ. 

Data owners have to deal with a number of legal issues—for example, the liability they absorb as contractors—that extends to sourcing data to the public sector or third parties, such as navigation and transportation service providers. It is important to note for an IOO whether to absorb the liability risk of CWZ data, since most IOOs pass on the general risk of work zones onto contractors. 

## **Guidance Needs – Licensing [B.2.2.2]** 

One concern data owners have is determining who has rights to the data when it is aggregated. Limiting a data consumer's rights to redistribution of data protects data owners. Licensing the data provides clarification on restrictions related to the data's usage and may include limited rights to re-distribute the data or to save the data for historical analysis purposes. 

It is important for licensees, especially IOOs, to understand the constraints stated in a data license. CWZ deployers will need to think about their long-term goals to identify the impacts of the limitations and constraints that are enacted in a license. It is noteworthy that while accepting a license limits usage, it also limits exposure to liability risk. 

**Rationale:** CWZ WG Discussion. 

- There were questions about why this section is in a standard. 

- This is about contracting. Keep contracting out of this document. 

- This section should not be contracting guidance. 

- Perhaps re-characterize that what IOOs need is to establish a “pre-qualification” process. 

- There was a suggestion to separate the discussion on Contracting from the discussion on Data Ownership and Licensing 

- There was a question as to whether this would only apply to pilot projects. 

- There was a suggestion that maybe a discussion about qualified products lists is better. 

- There is a lot of equipment out there and is being tested. Recommend that agencies accept testing done in other States. 

- One issue is that if IOOs do not require (emphasis on the term require) the CWZ equipment, then this equipment is less likely to be deployed in a WZ. 

- One person suggested broadening the discussion to include all those that will benefit. 

- There was a question as to why it is necessary to 'single out' IOOs in this section. 

- Some IOOs are requiring the use of electronic work zone equipment. 

- There was clarification that this section is not intending to mandate anything. 

- One benefit is assisting with the inspection process. The equipment manufacturers can facilitate the process to verify the equipment is in fact working. 

- It is important to show the value – e.g., to consumers, to OEMs – and that that value comes at an additional cost when you deploy electronic equipment. 

- Many will shrug at the guidance and 'recommendations'. The goal should be for deployers to figure out how to make their data fit the requirements in the standard. 

- We have to remember that each IOO is different, and they should not be lumped together. 

- What's important is to focus not on the equipment, but rather on the work zone features required and data you need to collect and share. Let the features drive the equipment choices. 

- There was some concern about why we are discussing Data Ownership and Licensing? 

- One person offered an example: For DeviceFeed information, we (equipment vendor) need to specify ownership of the data, and the limitations of sharing the data with others. 

Typically, for IOOs, if the device feed matches a planned project, then that becomes part of the agency's WZFeed, and that is the only data that the agency can distribute. For a navigation company, the agreement may be completely different. 

- There was clarification that an agency's WZFeed is a public resource and should be freely available. All agreed. 

- There was more concern about whether this topic should be included in this guidance. 

- There was additional support for the statement that the WZFeed shall be freely available 

   - and that this should be stated in an agreement. 

- The WG collectively agreed to remove this section after much discussion. 

