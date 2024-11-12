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
job_description VARCHAR(2000),
company_rating VARCHAR(10),
link_to_application VARCHAR(500)
);

CREATE TABLE work_experiences (
    work_experience_id SERIAL,
	user_id INT,
    job_title VARCHAR(50),
    company VARCHAR(50),
    start_date DATE,
    end_date DATE,
    city VARCHAR(60),
	country VARCHAR(20),
    job_description VARCHAR(200),
    PRIMARY KEY(user_id, work_experience_id),
	FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE TABLE education (
    education_id SERIAL,
	user_id INT,
    university VARCHAR(50),
    degree VARCHAR(50),
    graduation_year NUMERIC(4,0),
    GRADE varchar(10),
    PRIMARY KEY(user_id, education_id),
	FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE TABLE certifications (
    certification_id SERIAL,
	user_id INT,
    certificate VARCHAR(50),
    PRIMARY KEY(user_id, certification_id),
	FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE TABLE projects (
    project_id SERIAL,
	user_id INT,
    start_date DATE,
    end_Date DATE,
    description VARCHAR(200),
    PRIMARY KEY(user_id, project_id),
	FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE TABLE skills (
    user_id INT PRIMARY KEY,
    skill VARCHAR[],
	FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE TABLE users_jobs(
user_id INT,
job_id INT,
saved_date DATE,
FOREIGN KEY (user_id) REFERENCES users(user_id),
FOREIGN KEY (job_id) REFERENCES jobs(job_id)
);

