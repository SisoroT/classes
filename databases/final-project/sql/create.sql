CREATE TABLE Teams (
    TeName VARCHAR(30) PRIMARY KEY,
    Coach VARCHAR(30),
    Owner VARCHAR(30)
);

CREATE TABLE Players (
    PlayerID VARCHAR(30) PRIMARY KEY,
    AccountLevel INT,
    Rank VARCHAR(30),
    TeName VARCHAR(20),
    FOREIGN KEY (TeName) REFERENCES Teams(TeName),
    CONSTRAINT playerid_format CHECK (playerid LIKE '%#%')
);

CREATE TABLE Statistics (
    StatisticsID INT PRIMARY KEY,
    PlayerID VARCHAR(30),
    Kills INT,
    Deaths INT,
    WinPCT INT,
    HeadshotPCT INT,
    FOREIGN KEY (PlayerID) REFERENCES Players(PlayerID)
);

CREATE TABLE Skins (
    SName VARCHAR(60) PRIMARY KEY,
    Rarity VARCHAR(20),
    Price INT,
    Weapon VARCHAR(20)
);

CREATE TABLE Buy (
    PlayerID VARCHAR(60),
    SName VARCHAR(20),
    PRIMARY KEY (PlayerID, SName),
    FOREIGN KEY (PlayerID) REFERENCES Players(PlayerID),
    FOREIGN KEY (SName) REFERENCES Skins(SName)
);

CREATE TABLE Agents (
    AName VARCHAR(60) PRIMARY KEY,
    Ultimate VARCHAR(30),
    Ability1 VARCHAR(30),
    Ability2 VARCHAR(30),
    Ability3 VARCHAR(30),
    Role VARCHAR(30)
);

CREATE TABLE Own (
    PlayerID VARCHAR(60),
    AName VARCHAR(60),
    PRIMARY KEY (PlayerID, AName),
    FOREIGN KEY (PlayerID) REFERENCES Players(PlayerID),
    FOREIGN KEY (AName) REFERENCES Agents(AName)
);

CREATE TABLE Companies (
    CName VARCHAR(30) PRIMARY KEY,
    Industry VARCHAR(30)
);

CREATE TABLE Sponsor (
    TeName VARCHAR(30),
    CName VARCHAR(30),
    PRIMARY KEY (TeName, CName),
    FOREIGN KEY (TeName) REFERENCES Teams(TeName),
    FOREIGN KEY (CName) REFERENCES Companies(CName)
);

CREATE TABLE Tourneys (
    TName VARCHAR(30) PRIMARY KEY,
    Location VARCHAR(30),
    CashPrize INT
);

CREATE TABLE Compete_In (
    TeName VARCHAR(30),
    TName VARCHAR(30),
    PRIMARY KEY (TeName, TName),
    FOREIGN KEY (TeName) REFERENCES Teams(TeName),
    FOREIGN KEY (TName) REFERENCES Tourneys(TName)
);

CREATE TABLE Modes (
    MoName VARCHAR(30) PRIMARY KEY,
    Rules VARCHAR(30),
    Objectives VARCHAR(30)
);

CREATE TABLE Contain (
    TName VARCHAR(30),
    MoName VARCHAR(30),
    PRIMARY KEY (TName, MoName),
    FOREIGN KEY (TName) REFERENCES Tourneys(TName),
    FOREIGN KEY (MoName) REFERENCES Modes(MoName)
);

CREATE TABLE Series (
    SeriesID INT PRIMARY KEY,
    MoName VARCHAR(30),
    Competitor1 VARCHAR(30),
    Competitor2 VARCHAR(30),
    C1Score VARCHAR(2),
    C2Score VARCHAR(2),
    Length INT,
    Date VARCHAR(20),
    FOREIGN KEY (MoName) REFERENCES Modes(MoName)
);

CREATE TABLE Maps (
    MaName VARCHAR(30) PRIMARY KEY,
    C1Score VARCHAR(2),
    C2Score VARCHAR(2)
);

CREATE TABLE Played_On (
    SeriesID INT,
    MaName VARCHAR(30),
    PRIMARY KEY (SeriesID, MaName),
    FOREIGN KEY (SeriesID) REFERENCES Series(SeriesID),
    FOREIGN KEY (MaName) REFERENCES Maps(MaName)
);

CREATE TABLE Callouts (
    CalloutID INT PRIMARY KEY,
    Name VARCHAR(30),
    Location VARCHAR(30),
    MaName VARCHAR(30),
    FOREIGN KEY (MaName) REFERENCES Maps(MaName)
);
