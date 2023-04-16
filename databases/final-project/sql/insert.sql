-- Teams
INSERT INTO Teams (TeName, Coach, Owner) VALUES ('TeamSoloMid', 'JohnDoe', 'Reginald');
INSERT INTO Teams (TeName, Coach, Owner) VALUES ('Sentinels', 'JaneSmith', 'RobHanner');

-- Players
INSERT INTO Players (PlayerID, AccountLevel, Rank, TeName) VALUES ('Wardell#1234', 500, 'Radiant', 'TeamSoloMid');
INSERT INTO Players (PlayerID, AccountLevel, Rank, TeName) VALUES ('Subroza#5678', 490, 'Radiant', 'TeamSoloMid');
INSERT INTO Players (PlayerID, AccountLevel, Rank, TeName) VALUES ('Sinatraa#1357', 480, 'Radiant', 'Sentinels');
INSERT INTO Players (PlayerID, AccountLevel, Rank, TeName) VALUES ('Shazam#2468', 470, 'Radiant', 'Sentinels');

-- Statistics
INSERT INTO Statistics (StatisticsID, PlayerID, Kills, Deaths, WinPCT, HeadshotPCT) VALUES (1, 'Wardell#1234', 5000, 3000, 66, 54);
INSERT INTO Statistics (StatisticsID, PlayerID, Kills, Deaths, WinPCT, HeadshotPCT) VALUES (2, 'Subroza#5678', 4800, 3200, 52, 58);
INSERT INTO Statistics (StatisticsID, PlayerID, Kills, Deaths, WinPCT, HeadshotPCT) VALUES (3, 'Sinatraa#1357', 5200, 2800, 79, 80);
INSERT INTO Statistics (StatisticsID, PlayerID, Kills, Deaths, WinPCT, HeadshotPCT) VALUES (4, 'Shazam#2468', 4900, 3100, 84, 70);

-- Skins
INSERT INTO Skins (SName, Rarity, Price, Weapon) VALUES ('Reaver Vandal', 'Legendary', 1775, 'Vandal');
INSERT INTO Skins (SName, Rarity, Price, Weapon) VALUES ('Prime Spectre', 'Legendary', 1775, 'Spectre');

-- Buy
INSERT INTO Buy (PlayerID, SName) VALUES ('Wardell#1234', 'Reaver Vandal');
INSERT INTO Buy (PlayerID, SName) VALUES ('Subroza#5678', 'Prime Spectre');
INSERT INTO Buy (PlayerID, SName) VALUES ('Sinatraa#1357', 'Reaver Vandal');
INSERT INTO Buy (PlayerID, SName) VALUES ('Shazam#2468', 'Prime Spectre');

-- Agents
INSERT INTO Agents (AName, Ultimate, Ability1, Ability2, Ability3, Role) VALUES ('Jett', 'Blade Storm', 'Cloudburst', 'Updraft', 'Tailwind', 'Duelist');
INSERT INTO Agents (AName, Ultimate, Ability1, Ability2, Ability3, Role) VALUES ('Sage', 'Resurrection', 'Healing Orb', 'Slow Orb', 'Barrier Orb', 'Sentinel');

-- Own
INSERT INTO Own (PlayerID, AName) VALUES ('Wardell#1234', 'Jett');
INSERT INTO Own (PlayerID, AName) VALUES ('Subroza#5678', 'Sage');
INSERT INTO Own (PlayerID, AName) VALUES ('Sinatraa#1357', 'Jett');
INSERT INTO Own (PlayerID, AName) VALUES ('Shazam#2468', 'Sage');

-- Companies
INSERT INTO Companies (CName, Industry) VALUES ('Logitech', 'Gaming Hardware');
INSERT INTO Companies (CName, Industry) VALUES ('Intel', 'Semiconductors');

-- Sponsor
INSERT INTO Sponsor (TeName, CName) VALUES ('TeamSoloMid', 'Logitech');
INSERT INTO Sponsor (TeName, CName) VALUES ('Sentinels', 'Intel');

-- Tourneys
INSERT INTO Tourneys (TName, Location, CashPrize) VALUES ('Valorant Masters', 'New York', 100000);
INSERT INTO Tourneys (TName, Location, CashPrize) VALUES ('Valorant Challengers', 'Los Angeles', 50000);

-- Compete_In
INSERT INTO Compete_In (TeName, TName) VALUES ('TeamSoloMid', 'Valorant Masters');
INSERT INTO Compete_In (TeName, TName) VALUES ('Sentinels', 'Valorant Masters');

-- Modes
INSERT INTO Modes (MoName, Rules, Objectives) VALUES ('Spike Rush', 'Best of 4', 'Plant/Defuse Spike');
INSERT INTO Modes (MoName, Rules, Objectives) VALUES ('Competitive', 'Best of 25', 'Plant/Defuse Spike');

-- Contain
INSERT INTO Contain (TName, MoName) VALUES ('Valorant Masters', 'Competitive');
INSERT INTO Contain (TName, MoName) VALUES ('Valorant Challengers', 'Spike Rush');

-- Series
INSERT INTO Series (SeriesID, MoName, Competitor1, Competitor2, C1Score, C2Score, Length, Date) VALUES (1, 'Competitive', 'TeamSoloMid', 'Sentinels', '3', '2', 50, '2023-04-20');

-- Maps
INSERT INTO Maps (MaName, C1Score, C2Score) VALUES ('Ascent', '13', '11');
INSERT INTO Maps (MaName, C1Score, C2Score) VALUES ('Bind', '10', '13');
INSERT INTO Maps (MaName, C1Score, C2Score) VALUES ('Haven', '13', '10');
INSERT INTO Maps (MaName, C1Score, C2Score) VALUES ('Split', '6', '13');
INSERT INTO Maps (MaName, C1Score, C2Score) VALUES ('Icebox', '13', '8');

-- Played_On
INSERT INTO Played_On (SeriesID, MaName) VALUES (1, 'Ascent');
INSERT INTO Played_On (SeriesID, MaName) VALUES (1, 'Bind');
INSERT INTO Played_On (SeriesID, MaName) VALUES (1, 'Haven');
INSERT INTO Played_On (SeriesID, MaName) VALUES (1, 'Split');
INSERT INTO Played_On (SeriesID, MaName) VALUES (1, 'Icebox');

-- Callouts
-- for Ascent
INSERT INTO Callouts (CalloutID, Name, Location, MaName) VALUES (1, 'A Main', 'A site', 'Ascent');
INSERT INTO Callouts (CalloutID, Name, Location, MaName) VALUES (2, 'B Main', 'B site', 'Ascent');
INSERT INTO Callouts (CalloutID, Name, Location, MaName) VALUES (3, 'Catwalk', 'Mid', 'Ascent');
INSERT INTO Callouts (CalloutID, Name, Location, MaName) VALUES (4, 'A Ramps', 'A site', 'Ascent');
INSERT INTO Callouts (CalloutID, Name, Location, MaName) VALUES (5, 'B Main', 'B site', 'Ascent');

-- for Bind
INSERT INTO Callouts (CalloutID, Name, Location, MaName) VALUES (6, 'B Lamps', 'B site', 'Bind');
INSERT INTO Callouts (CalloutID, Name, Location, MaName) VALUES (7, 'A Showers', 'A site', 'Bind');
INSERT INTO Callouts (CalloutID, Name, Location, MaName) VALUES (8, 'B Hookah', 'B site', 'Bind');

-- for Haven
INSERT INTO Callouts (CalloutID, Name, Location, MaName) VALUES (9, 'A Heaven', 'A site', 'Haven');
INSERT INTO Callouts (CalloutID, Name, Location, MaName) VALUES (10, 'A Short', 'A site', 'Haven');
INSERT INTO Callouts (CalloutID, Name, Location, MaName) VALUES (11, 'B Main', 'B site', 'Haven');
INSERT INTO Callouts (CalloutID, Name, Location, MaName) VALUES (12, 'C Long', 'C site', 'Haven');

-- for Split
INSERT INTO Callouts (CalloutID, Name, Location, MaName) VALUES (13, 'A Rafters', 'A site', 'Split');
INSERT INTO Callouts (CalloutID, Name, Location, MaName) VALUES (14, 'B Garage', 'B site', 'Split');
INSERT INTO Callouts (CalloutID, Name, Location, MaName) VALUES (15, 'Mid Market', 'Mid', 'Split');

-- for Icebox
INSERT INTO Callouts (CalloutID, Name, Location, MaName) VALUES (16, 'A Tower', 'A site', 'Icebox');
INSERT INTO Callouts (CalloutID, Name, Location, MaName) VALUES (17, 'B Elbow', 'B site', 'Icebox');
INSERT INTO Callouts (CalloutID, Name, Location, MaName) VALUES (18, 'B Tunnels', 'B site', 'Icebox');
