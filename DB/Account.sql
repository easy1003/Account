create database IF NOT EXISTS account;

use account;

CREATE TABLE IF NOT EXISTS `ACC_USER`(
  `ID`        INT UNSIGNED      AUTO_INCREMENT          COMMENT '用户ID',
  `USERNAME`  VARCHAR(32)       NOT NULL                COMMENT '用户名',
  `PASSWORD`  VARCHAR(32)       NOT NULL                COMMENT '密码',
  `REALNAME`  VARCHAR(32)                               COMMENT '真实姓名',
  `NICKNAME`  VARCHAR(32)                               COMMENT '昵称',
  `AVATAR`    VARCHAR(20)                               COMMENT '头像路径',
  `SIGNATURE` text                                      COMMENT '个性签名',
  `WX_ID`     VARCHAR(30)                               COMMENT '微信OpenID',
  `SEX`       tinyint(3) unsigned NOT NULL DEFAULT '0'  COMMENT '性别, 0无可奉告1女2男',
  `BIRTHDAY`  date        DEFAULT '2019-1-1'            COMMENT '生日',
  `MOBILE`    VARCHAR(15) NOT NULL                      COMMENT '用户手机',
  `STATUS`    tinyint(4)  DEFAULT '1'                   COMMENT '用户状态',
  PRIMARY KEY (`ID`),
  INDEX `NICKNAME` (`NICKNAME`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='用户表';

INSERT INTO ACC_USER (
ID,
USERNAME,
PASSWORD,
REALNAME,
NICKNAME,
AVATAR,
SIGNATURE,
WX_ID,
SEX,
BIRTHDAY,
MOBILE,
STATUS
)VALUES(
'1',
'ACCOUNT_TEST',
'123456',
'SPOCK',
'HELLO',
'TEST',
'NICE TO MEET YOU',
'WX_ID123',
'2',
'2019-1-15',
'18888888888',
'1'
);

