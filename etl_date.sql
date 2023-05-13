use example 
go
DECLARE @StartDate date; 
DECLARE @EndDate date;

SELECT @StartDate = '2015-01-01', @EndDate = '2035-12-31';

DECLARE @DateInProcess date = @StartDate;
DECLARE @counter int = 1;

WHILE @DateInProcess <= @EndDate
BEGIN
  -- Check if a row already exists for this date
  IF NOT EXISTS (SELECT * FROM [dbo].[DIM_Date] WHERE [dateID] = @counter)
  BEGIN
    -- Add a row into the date dimension table for this date
    INSERT INTO [dbo].[DIM_Date] 
    ( 
      [dateID],
      [Year],
      [Month],
      [Day]
    )
    VALUES ( 
      @counter, 
      CAST(YEAR(@DateInProcess) AS int), 
      CAST(MONTH(@DateInProcess) AS int), 
      CAST(DAY(@DateInProcess) AS int)
    );  
  END

  -- Add a day and loop again
  SET @counter = @counter + 1;
  SET @DateInProcess = DATEADD(d, 1, @DateInProcess);
END
