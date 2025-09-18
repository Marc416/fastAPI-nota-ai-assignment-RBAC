-- Experiment

-- L
CREATE TABLE experiment (
    id INT AUTO_INCREMENT PRIMARY KEY,
    experiment_id VARCHAR(36) UNIQUE NOT NULL,
    title VARCHAR(255) NOT NULL
);


--
INSERT INTO experiment (experiment_id, title) VALUES
(UUID(), '1'),
(UUID(), '2'),
(UUID(), '3');