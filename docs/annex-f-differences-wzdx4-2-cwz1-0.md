# **Annex F** 

# **Listing of Differences between the CWZ Standard and the WZDX v4.2 Specification JSON Schemas [Informative]** 

This annex lists differences between the JSON Schemas contained in Section 5 of this standard and the WZDX v4.2 Specification JSON Schemas. 

## **F.1 Differences Affecting Both the WorkZoneFeed and DeviceFeed** 

1. Replaced the use of GeoJSON ‘MultiPoint’ type with ‘Point’ as follows: The Geometry object's 'type' property MUST be LineString (RFC 7946 Section 3.1.4) or Point (RFC 7946 Section 3.1.2). 

2. Changed ‘feed_info’ to required because ‘road_event_feed_info’ was deprecated. 

3. Changed ‘update_frequency’ to required. 

4. Changed ‘update_frequency’ minimum value ‘1’ to ‘-1’. 

5. Changed ‘update_date’ to required. 

6. Removed deprecated element ‘lrs_type’. 

7. Removed deprecated element ‘lrs_url’. 

8. Removed deprecated element ‘location_verify_method’. 

9. Corrected typographical error of “verfied” to “verified” throughout. 

10. Removed ‘restriction’ as an enumerated value of ‘EventType’. 

11. Changed ‘milepost’ to ‘reference_post’ throughout. 

12. Added ‘reference_post_unit’ element. 

13. Updated the ‘reference_post_unit’ element to include ‘miles’. 

14. Added Operational Policy and Constraint that states that the assignment of UUIDs is governed by the regulatory guidelines and policies of the data provider. For example, the assignment of uniform resource identifiers may be governed by policies to guarantee privacy. As a result, UUIDs may need to change over time. 

15. Added Business Rule that states that all universally unique identifiers must comply with the UUID standard (RFC4122) reference. 

16. Added ‘project_id’ element. 

## **F.2 WorkZoneFeed Differences** 

1. Changed ‘is_start_position_verified’ to required. 

2. Changed ‘is_end_position_verified’ to required. 

3. Changed ‘is_start_date_verified’ to required. 

4. Changed ‘is_end_date_verified’ to required. 

5. Removed deprecated element ‘relationship’. 

6. Removed deprecated element ‘lane_number’. 

7. Removed deprecated enumeration ‘SpatialVerification’. 

8. Removed deprecated enumeration ‘TimeVerification’. 

9. Removed deprecated enumeration ‘EventStatus’. 

10. Changed WorkTypeName enumeration text “maintenance” to “non-encroachment”. 

11. Removed deprecated enumerated item ‘center-left-turn-lane’ from ‘LaneType’. 

## **F.3 DeviceFeed Differences** 

1. Removed deprecated element ‘is_moving’. 

2. Removed enumerated item ‘road-event-start’ from ‘MarkedLocationType’ 

3. Removed enumerated item ‘road-event-end’ from ‘MarkedLocationType’. 

4. Removed deprecated enumerated item ‘temporary-traffic-signal’ from ‘MarkedLocationType’. 

5. Added new enumerated items for vehicle types and ‘other’ to ‘MarkedLocationType’. 

6. Added enumerated item ‘pavement-marking-vehicle’ to ‘MarkedLocationType’. 

7. Added ‘is_in_transport_position’ to FieldDeviceCoreDetails to reflect that other devices (in addition to the ArrowBoard device) may have the characteristic of being in transport position. 

8. Removed ‘is_in_transport_position’ from ArrowBoard device. 

9. Added ‘is_image_url_public’ to contents of the Camera device. 

10. Added ‘video_url’ to contents of the Camera device. 

11. Added ‘is_video_url_public’ to contents of the Camera device. 

12. Added ‘video_update_frequency’ element to contents of Camera device to reflect how often video is updated. 

13. Added ‘RoadsideUnit’ as a new device. 

14. Added ‘roadside-unit’ enumerated item to ‘FieldDeviceType’. 

15. Added element ‘message_types’ to identify message being broadcast by an RSU (e.g., RSM, TIM, SPaT, MAP). Added enumerated list of potential RSU messages that could be broadcast. 

§ 

