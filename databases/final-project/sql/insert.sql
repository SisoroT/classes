-- Teams
INSERT INTO Teams (TeName, Coach, Owner) VALUES ('TeamSoloMid', 'JohnDoe', 'Reginald');
INSERT INTO Teams (TeName, Coach, Owner) VALUES ('Sentinels', 'JaneSmith', 'RobHanner');
INSERT INTO Teams (TeName, Coach, Owner) VALUES ('Cloud9', 'AliceJones', 'JackEtienne');
INSERT INTO Teams (TeName, Coach, Owner) VALUES ('100Thieves', 'TomBrown', 'Nadeshot');

-- Players
INSERT INTO Players (PlayerID, AccountLevel, Rank, TeName) VALUES ('Wardell#1234', 500, 'Radiant', 'TeamSoloMid');
INSERT INTO Players (PlayerID, AccountLevel, Rank, TeName) VALUES ('Subroza#5678', 490, 'Radiant', 'TeamSoloMid');
INSERT INTO Players (PlayerID, AccountLevel, Rank, TeName) VALUES ('Sinatraa#1357', 480, 'Radiant', 'Sentinels');
INSERT INTO Players (PlayerID, AccountLevel, Rank, TeName) VALUES ('Shazam#2468', 470, 'Radiant', 'Sentinels');
INSERT INTO Players (PlayerID, AccountLevel, Rank, TeName) VALUES ('TenZ#9632', 510, 'Radiant', 'Cloud9');
INSERT INTO Players (PlayerID, AccountLevel, Rank, TeName) VALUES ('Hiko#8521', 505, 'Radiant', '100Thieves');
INSERT INTO Players (PlayerID, AccountLevel, Rank, TeName) VALUES ('Asuna#7894', 498, 'Radiant', '100Thieves');
INSERT INTO Players (PlayerID, AccountLevel, Rank, TeName) VALUES ('Leaf#5312', 515, 'Radiant', 'Cloud9');

-- Statistics
INSERT INTO Statistics (StatisticsID, PlayerID, Kills, Deaths, WinPCT, HeadshotPCT) VALUES (1, 'Wardell#1234', 5000, 3000, 66, 54);
INSERT INTO Statistics (StatisticsID, PlayerID, Kills, Deaths, WinPCT, HeadshotPCT) VALUES (2, 'Subroza#5678', 4800, 3200, 52, 58);
INSERT INTO Statistics (StatisticsID, PlayerID, Kills, Deaths, WinPCT, HeadshotPCT) VALUES (3, 'Sinatraa#1357', 5200, 2800, 79, 80);
INSERT INTO Statistics (StatisticsID, PlayerID, Kills, Deaths, WinPCT, HeadshotPCT) VALUES (4, 'Shazam#2468', 4900, 3100, 84, 70);
INSERT INTO Statistics (StatisticsID, PlayerID, Kills, Deaths, WinPCT, HeadshotPCT) VALUES (5, 'TenZ#9632', 5300, 2700, 85, 60);
INSERT INTO Statistics (StatisticsID, PlayerID, Kills, Deaths, WinPCT, HeadshotPCT) VALUES (6, 'Hiko#8521', 5100, 2900, 80, 62);
INSERT INTO Statistics (StatisticsID, PlayerID, Kills, Deaths, WinPCT, HeadshotPCT) VALUES (7, 'Asuna#7894', 4800, 3100, 73, 52);
INSERT INTO Statistics (StatisticsID, PlayerID, Kills, Deaths, WinPCT, HeadshotPCT) VALUES (8, 'Leaf#5312', 5200, 2800, 77, 55);

-- Skins
INSERT INTO Skins (SName, Rarity, Price, Weapon) VALUES ('Reaver Vandal', 'Legendary', 1775, 'Vandal');
INSERT INTO Skins (SName, Rarity, Price, Weapon) VALUES ('Prime Spectre', 'Legendary', 1775, 'Spectre');
INSERT INTO Skins (SName, Rarity, Price, Weapon) VALUES ('Glitchpop Phantom', 'Legendary', 1775, 'Phantom');
INSERT INTO Skins (SName, Rarity, Price, Weapon) VALUES ('Oni Guardian', 'Legendary', 1775, 'Guardian');

-- Buy
INSERT INTO Buy (PlayerID, SName) VALUES ('Wardell#1234', 'Reaver Vandal');
INSERT INTO Buy (PlayerID, SName) VALUES ('Subroza#5678', 'Prime Spectre');
INSERT INTO Buy (PlayerID, SName) VALUES ('Sinatraa#1357', 'Reaver Vandal');
INSERT INTO Buy (PlayerID, SName) VALUES ('Shazam#2468', 'Prime Spectre');
INSERT INTO Buy (PlayerID, SName) VALUES ('TenZ#9632', 'Glitchpop Phantom');
INSERT INTO Buy (PlayerID, SName) VALUES ('Hiko#8521', 'Oni Guardian');
INSERT INTO Buy (PlayerID, SName) VALUES ('Asuna#7894', 'Reaver Vandal');
INSERT INTO Buy (PlayerID, SName) VALUES ('Leaf#5312', 'Prime Spectre');

-- Agents
INSERT INTO Agents (AName, Ultimate, Ability1, Ability2, Ability3, Role) VALUES ('Jett', 'Blade Storm', 'Cloudburst', 'Updraft', 'Tailwind', 'Duelist');
INSERT INTO Agents (AName, Ultimate, Ability1, Ability2, Ability3, Role) VALUES ('Sage', 'Resurrection', 'Healing Orb', 'Slow Orb', 'Barrier Orb', 'Sentinel');
INSERT INTO Agents (AName, Ultimate, Ability1, Ability2, Ability3, Role) VALUES ('Phoenix', 'Run it Back', 'Hot Hands', 'Blaze', 'Curveball', 'Duelist');
INSERT INTO Agents (AName, Ultimate, Ability1, Ability2, Ability3, Role) VALUES ('Cypher', 'Neural Theft', 'Trapwire', 'Cyber Cage', 'Spycam', 'Sentinel');

-- Own
INSERT INTO Own (PlayerID, AName) VALUES ('Wardell#1234', 'Jett');
INSERT INTO Own (PlayerID, AName) VALUES ('Subroza#5678', 'Sage');
INSERT INTO Own (PlayerID, AName) VALUES ('Sinatraa#1357', 'Jett');
INSERT INTO Own (PlayerID, AName) VALUES ('Shazam#2468', 'Sage');
INSERT INTO Own (PlayerID, AName) VALUES ('TenZ#9632', 'Jett');
INSERT INTO Own (PlayerID, AName) VALUES ('Hiko#8521', 'Cypher');
INSERT INTO Own (PlayerID, AName) VALUES ('Asuna#7894', 'Phoenix');
INSERT INTO Own (PlayerID, AName) VALUES ('Leaf#5312', 'Sage');

-- Companies
INSERT INTO Companies (CName, Industry) VALUES ('Logitech', 'Gaming Hardware');
INSERT INTO Companies (CName, Industry) VALUES ('Intel', 'Semiconductors');
INSERT INTO Companies (CName, Industry) VALUES ('NVIDIA', 'Technology');
INSERT INTO Companies (CName, Industry) VALUES ('Riot Games', 'Video Games');

-- Sponsor
INSERT INTO Sponsor (TeName, CName) VALUES ('TeamSoloMid', 'Logitech');
INSERT INTO Sponsor (TeName, CName) VALUES ('Sentinels', 'Intel');
INSERT INTO Sponsor (TeName, CName) VALUES ('Cloud9', 'NVIDIA');
INSERT INTO Sponsor (TeName, CName) VALUES ('100Thieves', 'Riot Games');

-- Tourneys
INSERT INTO Tourneys (TName, Location, CashPrize) VALUES ('Valorant Masters', 'New York', 100000);
INSERT INTO Tourneys (TName, Location, CashPrize) VALUES ('Valorant Challengers', 'Los Angeles', 50000);

-- Compete_In
INSERT INTO Compete_In (TeName, TName) VALUES ('TeamSoloMid', 'Valorant Masters');
INSERT INTO Compete_In (TeName, TName) VALUES ('Sentinels', 'Valorant Masters');
INSERT INTO Compete_In (TeName, TName) VALUES ('Cloud9', 'Valorant Challengers');
INSERT INTO Compete_In (TeName, TName) VALUES ('100Thieves', 'Valorant Challengers');

-- Modes
INSERT INTO Modes (MoName, Rules, Objectives) VALUES ('Spike Rush', 'Best of 4', 'Plant/Defuse Spike');
INSERT INTO Modes (MoName, Rules, Objectives) VALUES ('Competitive', 'Best of 25', 'Plant/Defuse Spike');
INSERT INTO Modes (MoName, Rules, Objectives) VALUES ('Unrated', 'Best of 25', 'Plant/Defuse Spike');
INSERT INTO Modes (MoName, Rules, Objectives) VALUES ('Escalation', 'Best of 7', 'Weapon-based Rounds');

-- Contain
INSERT INTO Contain (TName, MoName) VALUES ('Valorant Masters', 'Competitive');
INSERT INTO Contain (TName, MoName) VALUES ('Valorant Challengers', 'Spike Rush');
INSERT INTO Contain (TName, MoName) VALUES ('Valorant Challengers', 'Unrated');
INSERT INTO Contain (TName, MoName) VALUES ('Valorant Challengers', 'Escalation');

-- Series
INSERT INTO Series (SeriesID, MoName, Competitor1, Competitor2, C1Score, C2Score, Length, Date) VALUES (1, 'Competitive', 'TeamSoloMid', 'Sentinels', '3', '2', 120, '2023-04-20');
INSERT INTO Series (SeriesID, MoName, Competitor1, Competitor2, C1Score, C2Score, Length, Date) VALUES (2, 'Spike Rush', 'Cloud9', '100Thieves', '1', '0', 35, '2023-04-21');

-- Maps
INSERT INTO Maps (MaID, MaName, C1Score, C2Score, SeriesID) VALUES (1, 'Ascent', '13', '11', 1);
INSERT INTO Maps (MaID, MaName, C1Score, C2Score, SeriesID) VALUES (2, 'Bind', '10', '13', 1);
INSERT INTO Maps (MaID, MaName, C1Score, C2Score, SeriesID) VALUES (3, 'Haven', '13', '10', 1);
INSERT INTO Maps (MaID, MaName, C1Score, C2Score, SeriesID) VALUES (4, 'Split', '6', '13', 1);
INSERT INTO Maps (MaID, MaName, C1Score, C2Score, SeriesID) VALUES (5, 'Icebox', '13', '8', 1);
INSERT INTO Maps (MaID, MaName, C1Score, C2Score, SeriesID) VALUES (6, 'Bind', '10', '13', 2);

-- Callouts
-- for Ascent
INSERT INTO Callouts (CalloutID, Name, Location, MaID) VALUES (1, 'A Main', 'A site', 1);
INSERT INTO Callouts (CalloutID, Name, Location, MaID) VALUES (2, 'B Main', 'B site', 1);
INSERT INTO Callouts (CalloutID, Name, Location, MaID) VALUES (3, 'Catwalk', 'Mid', 1);
INSERT INTO Callouts (CalloutID, Name, Location, MaID) VALUES (4, 'A Ramps', 'A site', 1);
INSERT INTO Callouts (CalloutID, Name, Location, MaID) VALUES (5, 'B Main', 'B site', 1);

-- for Bind
INSERT INTO Callouts (CalloutID, Name, Location, MaID) VALUES (6, 'B Lamps', 'B site', 2);
INSERT INTO Callouts (CalloutID, Name, Location, MaID) VALUES (7, 'A Showers', 'A site', 2);
INSERT INTO Callouts (CalloutID, Name, Location, MaID) VALUES (8, 'B Hookah', 'B site', 2);

-- for Haven
INSERT INTO Callouts (CalloutID, Name, Location, MaID) VALUES (9, 'A Heaven', 'A site', 3);
INSERT INTO Callouts (CalloutID, Name, Location, MaID) VALUES (10, 'A Short', 'A site', 3);
INSERT INTO Callouts (CalloutID, Name, Location, MaID) VALUES (11, 'B Main', 'B site', 3);
INSERT INTO Callouts (CalloutID, Name, Location, MaID) VALUES (12, 'C Long', 'C site', 3);

-- for Split
INSERT INTO Callouts (CalloutID, Name, Location, MaID) VALUES (13, 'A Rafters', 'A site', 4);
INSERT INTO Callouts (CalloutID, Name, Location, MaID) VALUES (14, 'B Garage', 'B site', 4);
INSERT INTO Callouts (CalloutID, Name, Location, MaID) VALUES (15, 'Mid Market', 'Mid', 4);

-- for Icebox
INSERT INTO Callouts (CalloutID, Name, Location, MaID) VALUES (16, 'A Tower', 'A site', 5);
INSERT INTO Callouts (CalloutID, Name, Location, MaID) VALUES (17, 'B Elbow', 'B site', 5);
INSERT INTO Callouts (CalloutID, Name, Location, MaID) VALUES (18, 'B Tunnels', 'B site', 5);
