--CREATE TABLE DIM_contract (
--  contractID int PRIMARY KEY,
--  signing_date date,
--  active varchar(25),
--);

USE example
GO


If (object_id('view_contract') is not null) Drop View view_contract;
go
CREATE VIEW view_contract
AS
SELECT DISTINCT
	[contractID] as [c1],
	[signing_date] as [c2],
	CASE
		WHEN CAST(GETDATE() AS DATE) BETWEEN issue_date AND ending_date THEN 'ACTIVE'
		ELSE 'INACTIVE'
	END AS [c3]
FROM [kinder].dbo.contract
go


MERGE INTO DIM_contract as TT
	USING view_contract as ST
		ON TT.contractID = ST.c1
			WHEN Not Matched
				THEN
					INSERT
					Values (
					c1,c2,c3
					)
			--WHEN Not Matched By Source
			--	Then
			--		DELETE
					;

Drop View view_contract;
