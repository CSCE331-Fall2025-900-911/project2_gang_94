SELECT quantity, cost, expiration FROM ingredients as i JOIN onhandinventory as o 
ON  i.itemid = o.itemid WHERE estimated_reorder_date != reorderdate;