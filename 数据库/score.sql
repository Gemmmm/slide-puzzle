/*
Navicat SQL Server Data Transfer

Source Server         : sqlserver
Source Server Version : 105000
Source Host           : 127.0.0.1:1433
Source Database       : test
Source Schema         : dbo

Target Server Type    : SQL Server
Target Server Version : 105000
File Encoding         : 65001

Date: 2019-06-13 08:11:31
*/


-- ----------------------------
-- Table structure for score
-- ----------------------------
DROP TABLE [dbo].[score]
GO
CREATE TABLE [dbo].[score] (
[date_time] varchar(20) NULL ,
[score] varchar(20) NULL 
)


GO

-- ----------------------------
-- Records of score
-- ----------------------------
INSERT INTO [dbo].[score] ([date_time], [score]) VALUES (N'15:35:00', N'97')
GO
GO
INSERT INTO [dbo].[score] ([date_time], [score]) VALUES (N'15:36:00', N'98')
GO
GO
INSERT INTO [dbo].[score] ([date_time], [score]) VALUES (N'18:55:59', N'93')
GO
GO
INSERT INTO [dbo].[score] ([date_time], [score]) VALUES (N'18:57:50', N'90')
GO
GO
INSERT INTO [dbo].[score] ([date_time], [score]) VALUES (N'18:58:59', N'91')
GO
GO
INSERT INTO [dbo].[score] ([date_time], [score]) VALUES (N'18:59:20', N'99')
GO
GO
