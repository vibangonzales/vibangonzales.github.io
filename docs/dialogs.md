# 4 System Interface Design Details: Data Exchange Dialogs

## 4.1 Introduction \[Informative]

This section specifies the data exchange dialogs to be used with this standard.

## 4.2 Poll for Data Dialog

The Poll for Data Dialog is an HTTP-based mechanism used to transfer work zone information across a system interface. The subsections below enumerate the referenced standards and role of the standard specified for the Poll for Data Dialog.

### 4.2.1 GeoJSON Format – Geospatial Data Interchange Format based on JSON

The IETF RFC 7946 The GeoJSON Format is a normative reference of this standard.

The IETF RFC 7946 abstract contains the following definition.

"GeoJSON is a geospatial data interchange format based on JavaScript Object Notation (JSON). It defines several types of JSON objects and the manner in which they are combined to represent data about geographic features, their properties, and their spatial extents. GeoJSON uses a geographic coordinate reference system, World Geodetic System 1984, and units of decimal degrees."

GeoJSON is the data format for the Work Zone Feed and Device Feed.

### 4.2.2 JSON - JavaScript Object Notation

The IETF RFC 8259 The JavaScript Object Notation (JSON) Data Interchange Format, also known as ISO/IEC 21778:2017 is a normative reference of this standard.

The IETF RFC 8259 abstract contains the following definition.

"JavaScript Object Notation (JSON) is a lightweight, text-based, language-independent data interchange format. It was derived from the ECMAScript Programming Language Standard. JSON defines a small set of formatting rules for the portable representation of structured data.

The Work Zone Feed and Device Feed data are in JSON format and can be validated with a JSON Schema.

### 4.2.3 HTTP - HyperText Transfer Protocol

The IETF RFC 9110 HTTP Semantics is a normative reference of this standard. The IETF RFC 9110 HTTP outlines requirements and design principles, including the use of HTTP over TLS, a type of secure messaging protocol.

The IETF RFC 9110 abstract contains the following definition.

"The Hypertext Transfer Protocol (HTTP) is a stateless application-level protocol for distributed, collaborative, hypertext information systems. This document describes the overall architecture of HTTP, establishes common terminology, and defines aspects of the protocol that are shared by all versions. In this definition are core protocol elements, extensibility mechanisms, and the "http" and "https" Uniform Resource Identifier (URI) schemes.

HTTP is used to securely transmit Work Zone Feed and Device Feed data between two systems.

### 4.2.4 URI – Uniform Resource Identifier

The IETF RFC 3986 Uniform Resource Identifier (URI): Generic Syntax is a normative reference of this standard.

The IETF RFC 3986 abstract contains the following definition.

"A Uniform Resource Identifier (URI) is a compact sequence of characters that identifies an abstract or physical resource. This specification defines the generic URI syntax and a process for resolving URI references that might be in relative form, along with guidelines and security considerations for the use of URIs on the Internet. The URI syntax defines a grammar that is a superset of all valid URIs, allowing an implementation to parse the common components of a URI reference without knowing the scheme-specific requirements of every possible identifier. This specification does not define a generative grammar for URIs; that task is performed by the individual specifications of each URI scheme.

As described in Section 2.7.3 Operational Policies and Constraints – Uniform Resource Identifiers,

each feed provider defines their own URI based on their operational policies. It is the expectation of this standard that the URI defined by a data feed provider conforms with IETF RFC 3986.

