--finds the on hand inventories that expires in the next seven days
SELECT itemid, itemname, expiration
FROM onhandinventory
WHERE expiration < CURRENT_DATE + INTERVAL '7 days';