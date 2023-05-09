USE example
GO


If (object_id('[example].dbo.TEMPexcel') is not null) DROP TABLE [example].dbo.TEMPexcel;
CREATE TABLE [example].dbo.TEMPexcel(
applicationID int,
childID int, 
motherID int,
fatherID int,
date_meeting date,
hour time,
facilityID int
);
go

BULK INSERT [example].dbo.TEMPexcel
    FROM 'C:\Users\dedza\OneDrive\Pulpit\kamlek\4 SEM\DATA WARHOUSES\excel.csv'
    WITH
    (
    FIRSTROW = 1,
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',   
    TABLOCK
    );


If (object_id('view_junkNeed') is not null) Drop View view_junkNeed;
go
CREATE VIEW view_junkNeed
AS
SELECT DISTINCT
[kinder].dbo.application.applicationID as [id],
CASE
		WHEN [example].dbo.TEMPexcel.fatherID IS NULL OR
			[example].dbo.TEMPexcel.motherID IS NULL  THEN 'NOT_BOTH'
		ELSE 'BOTH'
	END as [parent],
CASE
		WHEN [example].dbo.TEMPexcel.fatherID IS NULL AND
			[example].dbo.TEMPexcel.motherID IS NULL  THEN 'CANCELLED'
		ELSE 'NOT_CANCELLED'
	END as [meeting],
CASE
		WHEN [kinder].dbo.application.issue_date =  [example].dbo.TEMPexcel.date_meeting
		THEN 'DURING'
		ELSE 'NOT_DURING'
	END as [during],
CASE
		WHEN [kinder].dbo.application.status = 0	
		THEN 'REJECTED'
		ELSE 'ACCEPTED'
	END as [status]
FROM [kinder].dbo.application
JOIN [example].dbo.TEMPexcel ON [example].dbo.TEMPexcel.applicationID = [kinder].dbo.application.applicationID
go


If (object_id('view_auxilary') is not null) Drop View view_auxilary;
go
CREATE VIEW view_auxilary
AS
SELECT DISTINCT 
[example].dbo.DIM_JUNK.JUNKID as [junkID],
[example].dbo.view_junkNeed.id as [appID]
FROM [example].dbo.DIM_JUNK
INNER JOIN [example].dbo.view_junkNeed ON 
[example].dbo.view_junkNeed.during = [example].dbo.DIM_JUNK.contract_durringmeeting AND
[example].dbo.view_junkNeed.meeting = [example].dbo.DIM_JUNK.meeting_cancelled AND
[example].dbo.view_junkNeed.parent = [example].dbo.DIM_JUNK.two_parents AND
[example].dbo.view_junkNeed.status = [example].dbo.DIM_JUNK.status_of_application
go


If (object_id('view_count') is not null) Drop View view_count;
go
CREATE VIEW view_count
AS
SELECT DISTINCT
applicationID as [id],
COUNT(*) as [counter]
FROM [kinder].dbo.application
JOIN [kinder].dbo.chooses ON [kinder].dbo.chooses.IDapplication = [kinder].dbo.application.applicationID
GROUP BY [kinder].dbo.application.applicationID
go


If (object_id('view_application') is not null) Drop View view_application;
go
CREATE VIEW view_application
AS
SELECT DISTINCT
applicationID as [c1],
[example].dbo.view_count.counter as [c2],
FK_facility  as [c3],
[kinder].dbo.chooses.choosesID as [c4],
[example].dbo.view_auxilary.junkID as [c5],
[kinder].dbo.contract.contractID as [c6],
[kinder].dbo.application.confirmation_date as [c7],
[kinder].dbo.application.issue_date as [c8],
[kinder].dbo.groups.groupID as [c9]
FROM [kinder].dbo.application 
LEFT JOIN [kinder].dbo.contract ON [kinder].dbo.application.applicationID = [kinder].dbo.contract.FK_application
LEFT JOIN  [kinder].dbo.child ON  [kinder].dbo.child.childID =  [kinder].dbo.application.FK_child
LEFT JOIN [kinder].dbo.groups ON [kinder].dbo.groups.groupID = [kinder].dbo.child.FK_groups
LEFT JOIN [kinder].dbo.chooses ON [kinder].dbo.chooses.IDapplication = [kinder].dbo.application.applicationID
LEFT JOIN [example].dbo.view_count ON [example].dbo.view_count.id = [kinder].dbo.application.applicationID
LEFT JOIN [example].dbo.view_auxilary ON [example].dbo.view_auxilary.appID = kinder.dbo.application.applicationID
go  


SELECT * FROM	view_application ORDER BY 1

MERGE INTO [example].dbo.FACT_NEWapplication as TT
	USING view_application as ST
		ON TT.applicationID = ST.c1
			WHEN Not Matched
				THEN
					INSERT
					Values (
					c1,c2,c3,c4,c5,c6,c7,c8,c9
					)
			--WHEN Not Matched By Source
			--	Then
			--		DELETE
					;
					

DROP VIEW view_application;
DROP VIEW view_auxilary;
DROP VIEW view_count;
DROP VIEW view_junkNeed;