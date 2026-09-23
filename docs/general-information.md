# 1 General Information \[Informative]

## 1.1 Scope

The purpose of ITE's Connected Work Zones project is to develop and publish a Connected Work Zone (CWZ) Implementation Guide and Standard that provides interoperable data exchanges among the various components of a connected work zone.

This CWZ Implementation Guide and Standard addresses gaps identified by early deployers and provides guidance for organizations seeking to develop interoperable connected work zones across the United States, especially for automated transportation systems. It focuses on harmonizing the existing Work Zone Data Exchange (WZDx) Specification, CWZ research and pilot deployments, and related standards activities addressing connected work zones.

The development of the CWZ Implementation Guide and Standard follows a systems engineering process, to be followed by a validation phase to verify the requirements and concepts in this guide. A report summarizing the findings will be developed to accompany this Guide.

## 1.2 References

At the time of publication, the indicated editions were valid. All standards are subject to revision, and parties to agreements based on the CWZ Implementation Guide and Standard are encouraged to consider applying the most recent editions of the standard listed.

### 1.2.1 Normative References

Normative references contain provisions that, through references in this text, form part of this CWZ Implementation Guide and Standard. Other references in this document may provide a complete understanding or additional information. At the time of publication, the indicated editions were valid. All standards are subject to revision, and parties to agreements based on this CWZ Implementation Guide and Standard are encouraged to consider applying the most recent editions of the standards listed.

|**Identifier**|**Title**|
|-|-|
|IETF RFC 7946|The GeoJSON Format, August 2016|
|IETF RFC 3339|Date and Time on the Internet: Timestamps, July 2002|
|IETF RFC 4122|A Universally Unique Identifier (UUID) URN Namespace, July 2005|
|IETF RFC 8259|The JavaScript Object Notation (JSON) Data Interchange Format, December 2017|
|IETF RFC 9110|HTTP Semantics, June 2022|
|IETF RFC 3986|Uniform Resource Identifier (URI): Generic Syntax, January 2005|
|Open Mobility Foundation|Curb Data Specification (CDS), v1.0.0, April 29, 2022|
|NTCIP 1203 v03|Object Definitions for Dynamic Message Signs (DMS), September 2014<br><br>\*For the definition of MULTI.|

### 1.2.2 Other References

The following documents and standards may provide the reader with a more complete understanding of connected work zones; however, these documents do not contain direct provisions that are required by the CWZ Implementation Guide and Standard.

|**Identifier**|**Title**|
|-|-|
|U.S. Architecture Reference for Cooperative and Intelligent Transportation (ARC-IT)|Architecture Reference for Cooperative and Intelligent Transportation (ARC-IT), USDOT, [http://local.iteris.com/arc-it/](http://local.iteris.com/arc-it/)|
|IEEE Std 610.12-1990|IEEE Standard Glossary of Software Engineering Terminology, IEEE, 1990|
|IEEE Std 829-2008|IEEE Std 829 IEEE Standard for Software and System Test Documentation, IEEE, 2008|
|IEEE Std 1016-1998|IEEE Recommended Practice for Software Design Descriptions, IEEE, 1998|
|IEEE Std 1362-1998|IEEE Guide for Information Technology System Definition – Concept of Operations (ConOps) Document, IEEE, 1998|
|FHWA MUTCD|The Manual on Uniform Traffic Control Devices for Streets and Highways, 2009.|
|NTCIP 1218 v01|National Transportation Communications for ITS Protocol Object Definitions for Roadside Units (RSUs), v01.38, 2020.|
|OMG UML-2007, Superstructure|OMG Unified Modeling Language (OMG UML), Superstructure, V2.1.2, 2007.|
|SAE J2945/4\_202305|Road Safety Applications, May 10, 2023|
|ITE/AASHTO TMDD Standard v3.1|Traffic Management Data Dictionary (TMDD) Standard for the<br><br>Center to Center Communications, January 13, 2020|
|USDOT WZDx v4.2|Work Zone Data Exchange Specification, USDOT, February 2023|
|NEMA TS 10|Connected Vehicle Infrastructure – Roadside Equipment, NEMA, March 2021|
|FHWA Work Zone ITS Implementation Guide 2014|Work Zone Intelligent Transportation Systems Implementation Guide – Use of Technology and Data for Effective Work Zone Management, January 2014|

### 1.2.3 Contact Information

The following sections provide contact information for publishers of documents referenced in this standard.

#### 1.2.3.1 ARC-IT Documents

The Architecture Reference for Cooperative and Intelligent Transportation (ARC-IT) may be viewed online at:

[https://local.iteris.com/arc-it/](https://local.iteris.com/arc-it/)

#### 1.2.3.2 FHWA Documents

USDOT Federal Highway Administration (FHWA) documents (with designations FHWA-JPO-…) are available at the USDOT National Transportation Library, Repository \& Open Science Access Portal (ROSA P):

[https://rosap.ntl.bts.gov/](https://rosap.ntl.bts.gov/)

#### 1.2.3.3 IEEE Standards

IEEE standards can be purchased online in electronic format or printed copy from the following:

Techstreet

6300 Interfirst Drive

Ann Arbor, MI 48108

(800) 699-9277

[www.techstreet.com/ieee](http://www.techstreet.com/ieee)

#### 1.2.3.4 Internet Documents

Obtain Request for Comment (RFC) electronic documents from several repositories on the World Wide Web, or by "anonymous" File Transfer Protocol (FTP) with several hosts. Browse or FTP to the following:

<www.rfc-editor.org>

[https://www.rfc-editor.org/retrieve/](https://www.rfc-editor.org/retrieve/)

#### 1.2.3.5 ITE Standards

Copies of ITE standards may be obtained from the following:

ITE- A Community of Transportation Professionals

1627 Eye Street, NW, Suite 600

Washington, DC 20006

(202) 785-0060

[www.ite.org/technical-resources/](http://www.ite.org/technical-resources/)

#### 1.2.3.6 NTCIP Standards

Copies of NTCIP standards may be obtained from the following:

NTCIP Coordinator

National Electrical Manufacturers Association

1300 N. 17th Street, Suite 900

Rosslyn, VA 22209-3801

<www.ntcip.org>

email: [ntcip@nema.org](mailto:ntcip@nema.org)

[https://www.ntcip.org/document-numbers-and-status/](https://www.ntcip.org/document-numbers-and-status/)

#### 1.2.3.7 SAE International Documents

Copies of SAE International documents may be obtained from the following:

SAE International  
400 Commonwealth Drive  
Warrendale, PA 15096

[www.sae.org](http://www.sae.org)

## 1.3 Terms

The following terms, definitions, acronyms, and abbreviations are used in this document.

<div class="joplin-table-wrapper"><table><thead><tr><th><p><strong>Term</strong></p></th><th><p><strong>Definition</strong></p></th></tr></thead><tbody><tr><td><p>Actor</p></td><td><p>An actor specifies a role played by a user or any other system that interacts with the subject.</p><p>Source: OMG UML-2007, Superstructure.</p></td></tr><tr><td><p>Component</p></td><td><p>One of the parts that make up a system. A component may be hardware or software and may be subdivided into other components.</p><p>Source: IEEE Std 610.12-1990<em>.</em></p></td></tr><tr><td><p>Connected Work Zone (CWZ)</p></td><td><p>A connected work zone is defined as a set of technologies that generates or collects work zone information (whether automatically or manually) and the infrastructure that broadcasts/distributes this information to the public and to vehicles.</p><p>Source: USDOT, Intelligent Transportation Systems (ITS) Joint Program Office Performance Work Statement for ITE's Connected Work Zone Implementation Guidance, 2022</p></td></tr><tr><td><p>CWZ Deployers</p></td><td><p>A collective term to describe IOOs, contractors, or any organization that deploys a CWZ, with responsibilities for actor components within a CWZ.</p></td></tr><tr><td><p>External Center</p></td><td><p>A center, whether virtual, mobile, or stationary, interacting with a Traffic Management Center or Work Zone Center. Typically used to describe a Third-Party Center, such as a back-office or cloud.</p></td></tr><tr><td><p>Generic Vehicle</p></td><td><p>A vehicle (passenger vehicle, van, bus, or truck) traveling through a connected work zone, but not associated with any activities within it.</p></td></tr><tr><td><p>Interface</p></td><td><p>A shared boundary across which information is passed.</p><p>Source: <em>IEEE Std 610.12-1990.</em></p></td></tr><tr><td><p>Interoperability</p></td><td><p>The ability of two or more systems or components to exchange information and to use the information that has been exchanged.</p><p>Source: <em>IEEE Std 610.12-1990.</em></p></td></tr><tr><td><p>Traffic Management Center</p></td><td><p>Centers, typically managed by IOOs, that tracs (collect) work zone status and conditions, and distribute Work Zone Information.</p></td></tr><tr><td><p>Universally Unique Identifier (UUID)</p></td><td><p>A UUID is 128 bits long and can guarantee uniqueness across space and time.</p><p>Source: <em>IETF RFC 4122.</em></p></td></tr><tr><td><p>Work Zone Center</p></td><td><p>Centers that directly collect information from Work Zone Field Devices, Work Zone VRUs, Work Zone Work Vehicles to generate a composite view of the status and conditions of a work zone.</p></td></tr><tr><td><p>Work Zone Device</p></td><td><p>Devices and electronic systems that monitor and affect work zone operations on a roadway. Examples include arrow boards, location marker devices, and roadside units (for connected vehicle environments).</p></td></tr><tr><td><p>Work Zone Vulnerable Road User (WZVRU)</p></td><td><p>A term to describe a class of persons at risk of harm within or near an active roadway, such as a work zone, i.e., those unprotected by an outside shield. In the case of a work zone, this may include work zone workers. This standard assumes that WZVRUs wear devices that are able to communicate with a work zone center, work zone equipment and/or vehicles.</p><p>Sub-categories of WZVRUs may include:</p><ul><li>Work Zone Workers</li><li>Non-workers passing through the work zone (e.g., individuals casually passing through)</li><li>Other Workers, including first responders and incident responders</li><li>Persons with disabilities</li></ul></td></tr><tr><td><p>Work Zone Work Vehicle</p></td><td><p>A term to describe a class of vehicles within or near an active roadway, such as a work zone. This may include maintenance vehicles, construction vehicles, attenuator vehicles, or in some cases first responder vehicles in a work zone. This standard assumes that work zone vehicles have devices that are able to communicate with a work zone center, work zone equipment, and/or vehicles.</p></td></tr></tbody></table></div>

## 1.4 Abbreviations

The abbreviations and acronyms used in this document are defined below.

|AASHTO|American Association of State Highway Transportation Officials|
|-|-|
|API|Application Programming Interface|
|ARC-IT|Architecture Reference for Cooperative and Intelligent Transportation|
|ATMS|Advanced Traffic Management System|
|CAMP|Collision Avoidance Metrics Partners|
|CWZ|Connected Work Zone|
|ConOps|Concept of Operations|
|C/AV|Connected/Automated Vehicle|
|C-V2X|Cellular Vehicle to Everything|
|CV|Connected Vehicle|
|CVE|Connected Vehicle Environment|
|DOT|Department of Transportation|
|DSRC|Dedicated Short Range Communication|
|FHWA|Federal Highway Administration|
|GeoJSON|Geospatial JSON (see JSON)|
|GIS|Geographic Information System|
|GNSS|Global Navigation Satellite System|
|IEEE|Institute of Electrical and Electronics Engineers|
|IOO|Infrastructure Owner/Operator|
|ICD|Interface Control Document|
|IT|Information Technology|
|ITE|Institute of Transportation Engineers|
|JSON|JavaScript Object Notation|
|LIDAR|Light Detection and Ranging (also LiDAR)|
|MPH|miles per hour|
|MUTCD|Manual of Uniform Traffic Control Devices|
|NEMA|National Electrical Manufacturers Association|
|ngTMDD|Next Generation Traffic Management Data Dictionary|
|NOCoE|National Operations Center of Excellence|
|NTCIP|National Transportation Communications for ITS Protocol|
|OBU|On-Board Unit|
|OEM|Automotive Original Equipment Manufacturer|
|PRL|Protocol Requirements List|
|RSM|Roadside Safety Message|
|RSU|Roadside Unit|
|RTCM|Radio Technical Commission for Maritime Services|
|RTM|Requirements Traceability Matrix|
|SAE|SAE International|
|SCMS|Security Credentials Management System|
|SDO|Standards Development Organization|
|SEP|Systems Engineering Process|
|TIM|Traveler Information Message|
|TIM-PM|Traffic Incident Management Performance Measures|
|TMDD|Traffic Management Data Dictionary|
|USDOT|United States Department of Transportation|
|UUID|Universally Unique Identifier|
|WZDx|Work Zone Data Exchange Specification|
|VRU|Vulnerable Road User|
|||

