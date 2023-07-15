-- script that creates a stored procedure ComputeAverageWeightedScoreForUser 
-- that computes and store the average weighted score for a student.

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;

DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUser (IN user_id INT)
BEGIN
    DECLARE sum_weights FLOAT;
    DECLARE weighted_sum FLOAT;

    SELECT SUM(weight) INTO sum_weights FROM projects;

    SELECT SUM(corrections.score * projects.weight) INTO weighted_sum
    FROM corrections
    JOIN projects ON corrections.project_id = projects.id
    WHERE corrections.user_id = user_id;

    UPDATE users SET average_score = weighted_sum / sum_weights WHERE id = user_id;
END $$

DELIMITER ;
