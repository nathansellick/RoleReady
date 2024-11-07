CREATE TABLE work_expereiences (
    user_id SERIAL,
    work_expereience_id SERIAL,
    job_title VARCHAR(50),
    company VARCHAR(50),
    start_date DATE,
    end_date DATE,
    location VARCHAR(60),
    job_description VARHCAR(200),
    PRIMARY KEY(user_id, work_expereience_id)
);

CREATE TABLE education (
    user_id SERIAL,
    education_id SERIAL,
    university VARCHAR(50),
    degree VARCHAR(50),
    graduation_year NUMBER(4,0),
    GRADE varchar(10),
    PRIMARY KEY(user_id, education_id)
);

CREATE TABLE certifications (
    user_id SERIAL,
    certification_id SERIAL,
    certificate VARCHAR(50),
    PRIMARY KEY(user_id, certification_id)
);

CREATE TABLE projects (
    user_id SERIAL,
    project_id SERIAL,
    start_date DATE,
    end_Date DATE,
    description VARCHAR(200)
    PRIMARY KEY(user_id, project_id)
);

CREATE TABLE skills (
    user_id SERIAL,
    skill_id SERIAL,
    skill INTEGER[]
    PRIMARY KEY(user_id, skill_id)
);