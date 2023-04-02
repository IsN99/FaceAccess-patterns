CREATE TABLE IF NOT EXISTS employees (
  id SERIAL PRIMARY KEY,
  name VARCHAR,
  photo_path VARCHAR
  
);

CREATE TABLE IF NOT EXISTS checkpoints (
  id SERIAL PRIMARY KEY,
  access_zone VARCHAR(50) NOT NULL
);

CREATE TABLE requests (
    id SERIAL PRIMARY KEY,
    date TIMESTAMP NOT NULL,	
    result BOOLEAN,
    image_path VARCHAR,
    checkpoint_id INTEGER REFERENCES checkpoints(id),
    employee_id INTEGER REFERENCES employees (id)
);


