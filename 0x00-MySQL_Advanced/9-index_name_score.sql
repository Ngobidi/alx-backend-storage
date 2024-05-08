-- develop an index idx_name_first_score on the table name and
-- the first letter of name and the scores.
CREATE INDEX idx_name_first_score ON names(name(1), score);
