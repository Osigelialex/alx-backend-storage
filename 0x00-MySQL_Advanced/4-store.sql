-- delete any existing trigger `decrease_quantity`
DROP TRIGGER  IF EXISTS decrease_quantity;

-- change delimiter to dollar sign
DELIMITER $$

-- create trigger to decrease quantity
-- of items after each order for the item
CREATE TRIGGER decrease_quantity 
AFTER INSERT ON orders FOR EACH ROW
-- decrease the quantity of item in items table
BEGIN
UPDATE items SET quantity = quantity - NEW.number
WHERE name = NEW.item_name;
END $$
