use example
go
If ((SELECT COUNT(*) FROM DIM_JUNK) < 2)
INSERT INTO [dbo].[DIM_JUNK] (two_parents, meeting_cancelled, contract_durringmeeting, status_of_application) VALUES
('BOTH', 'CANCELLED', 'DURING', 'REJECTED'),
('BOTH', 'CANCELLED', 'DURING', 'ACCEPTED'),
('BOTH', 'CANCELLED', 'NOT_DURING', 'REJECTED'),
('BOTH', 'CANCELLED', 'NOT_DURING', 'ACCEPTED'),
('BOTH', 'NOT_CANCELLED', 'DURING', 'REJECTED'),
('BOTH', 'NOT_CANCELLED', 'DURING', 'ACCEPTED'),
('BOTH', 'NOT_CANCELLED', 'NOT_DURING', 'REJECTED'),
('BOTH', 'NOT_CANCELLED', 'NOT_DURING', 'ACCEPTED'),
('NOT_BOTH', 'CANCELLED', 'DURING', 'REJECTED'),
('NOT_BOTH', 'CANCELLED', 'DURING', 'ACCEPTED'),
('NOT_BOTH', 'CANCELLED', 'NOT_DURING', 'REJECTED'),
('NOT_BOTH', 'CANCELLED', 'NOT_DURING', 'ACCEPTED'),
('NOT_BOTH', 'NOT_CANCELLED', 'DURING', 'REJECTED'),
('NOT_BOTH', 'NOT_CANCELLED', 'DURING', 'ACCEPTED'),
('NOT_BOTH', 'NOT_CANCELLED', 'NOT_DURING', 'REJECTED'),
('NOT_BOTH', 'NOT_CANCELLED', 'NOT_DURING', 'ACCEPTED')
go
