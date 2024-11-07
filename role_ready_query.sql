CREATE TABLE users(
user_id SERIAL PRIMARY KEY,
user_name VARCHAR(25) NOT NULL,
user_password VARCHAR(25) NOT NULL
);

CREATE TABLE jobs(
job_id SERIAL PRIMARY KEY,
job_title VARCHAR(50),
company_name VARCHAR(50),
location VARCHAR(60),
salary VARCHAR(25),
employment_type VARCHAR(50),
job_description VARCHAR(1000),
company_rating FLOAT,
link_to_application VARCHAR(100)
);

CREATE TABLE users_jobs(
user_id INT,
job_id INT,
saved_date DATE,
FOREIGN KEY (user_id) REFERENCES users(user_id),
FOREIGN KEY (job_id) REFERENCES jobs(job_id)
);





