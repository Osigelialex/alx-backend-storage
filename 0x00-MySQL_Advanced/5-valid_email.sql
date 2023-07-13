-- script that creates a trigger that resets 
-- the attribute valid_email only when the email has been changed.

-- delete existing trigger
DROP TRIGGER IF EXISTS valid_email;

-- create trigger
DELIMITER $$
CREATE TRIGGER valid_email
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
  IF NEW.email <> OLD.email THEN
    UPDATE users SET valid_email = DEFAULT WHERE email = OLD.email;
  END IF;
END $$
DELIMITER ;
