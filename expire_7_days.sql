SELECT itemid, itemname, expiration
FROM onhandinventory
WHERE expiration < CURRENT_DATE + INTERVAL '7 days';