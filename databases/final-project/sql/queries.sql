-- SELECT * FROM Players;
-- SELECT * FROM Teams;
-- SELECT * FROM Statistics;
-- SELECT * FROM Skins;
-- SELECT * FROM Buy;
-- SELECT * FROM Agents;
-- SELECT * FROM Own;
-- SELECT * FROM Companies;
-- SELECT * FROM Sponsor;
-- SELECT * FROM Tourneys;
-- SELECT * FROM Compete_In;
-- SELECT * FROM Modes;
-- SELECT * FROM Contain;
-- SELECT * FROM Series;
-- SELECT * FROM Maps;
-- SELECT * FROM Played_On;
-- SELECT * FROM Callouts;

-- 1. The database should let users create new tables that show only some parts of the data based on what they want to see.
CREATE VIEW PlayersAndTeams AS
SELECT
    PlayerID,
    TeName
FROM Players;
SELECT * FROM PlayersAndTeams;

-- 2. The database should let users combine data from different tables.
SELECT
    Players.PlayerID,
    Teams.TeName,
    Teams.Coach,
    Teams.Owner
FROM Players
INNER JOIN Teams ON Players.TeName = Teams.TeName;

-- 3. The database should let users get summary information or calculations for the data using functions such as count, sum, average etc.
SELECT
    TeName,
    AVG(WinPCT) AS AvgWinPCT,
    AVG(HeadshotPCT) AS AvgHeadshotPCT
FROM Statistics
JOIN Players ON Players.PlayerID = Statistics.PlayerID
GROUP BY TeName;

-- 4. The database should let users arrange or show the data in increasing or decreasing order based on one or more attributes.
SELECT
    PlayerID,
    HeadshotPCT
FROM Statistics
ORDER BY HeadshotPCT DESC;

-- 5. The database should let users choose which data they want to see based on some conditions or criteria using operators.
SELECT
    PlayerID,
    WinPCT
FROM Statistics
WHERE WinPCT >= 70;

-- 6. The database should ensure data integrity and consistency by enforcing referential integrity and domain constraints on the entities and attributes.
-- This will fail due to the domain constraint check in the `Players` table.
INSERT INTO Players (PlayerID, AccountLevel, Rank, TeName) VALUES ('NewPlayerID', 80, 'Radiant', 'TeamSoloMid');

-- 7. The database should support maintainability and extensibility by allowing users to update or modify the database schema or functionality without affecting the existing data or operations.
ALTER TABLE Players ADD Email VARCHAR(255);
SELECT * FROM Players;
