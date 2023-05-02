INSERT INTO [dbo].[DIM_JUNK] 
SELECT t, m, c, s 
FROM 
	  (
		VALUES 
			  ('PRESENT')
			, ('ABSENT')
		
	  ) 
	AS two_parents(t)
	, (
		VALUES 
			  ('CANCELLED')
			, ('NOT_CANCELLED')
	  ) 
	AS meeting_cancelled(m)
	, (
		VALUES 
			  ('SIGNED')
			, ('NOT')
		
	  ) 
	AS contract_durringmeeting(c)
	, (
		VALUES 
			  ('REJECTED')
			, ('ACCEPTED')
	 ) AS status_of_application(s);
	
SELECT * FROM DIM_JUNK
SELECT * FROM DIM_Date
SELECT * FROM DIM_contract