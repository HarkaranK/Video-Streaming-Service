-- init.sql

-- Create a table for storing video details
CREATE TABLE videos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    video_name VARCHAR(255) NOT NULL,
    video_path VARCHAR(255) NOT NULL
);

-- Sample data (optional)
INSERT INTO videos (video_name, video_path) VALUES ('SampleVideo', 'path/to/sample/video.mp4');
