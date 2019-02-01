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


CREATE TABLE IF NOT EXISTS `ACC_CATEGORY`(
    `ID` INT UNSIGNED AUTO_INCREMENT            COMMENT '类别ID',
    `CATEGORY` VARCHAR(32) NOT NULL             COMMENT '类别名称',
    `STATUS` tinyint(4)  DEFAULT '1'            COMMENT '状态',
    PRIMARY KEY (`ID`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='消费类别表';

CREATE TABLE IF NOT EXISTS `ACC_MONEY`(
    `ID` INT UNSIGNED AUTO_INCREMENT            COMMENT '币种ID',
    `MONEY` VARCHAR(100) NOT NULL               COMMENT '币种名称',
    `STATUS` tinyint(4)  DEFAULT '1'            COMMENT '状态',
    PRIMARY KEY (`ID`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='币种表';


CREATE TABLE IF NOT EXISTS `ACC_ACCOUNT` (
    `ID` INT UNSIGNED AUTO_INCREMENT            COMMENT '支出表ID',
    `LABEL` TINYINT(4) NOT NULL                 COMMENT '收入或支出',
    `CATEGORY` INT UNSIGNED NOT NULL            COMMENT '种类',
    `CONTENT` VARCHAR(100)                      COMMENT '支出明细',
    `NUM` INT UNSIGNED DEFAULT '0'              COMMENT '金额',
    `MONEY` INT UNSIGNED DEFAULT '1'            COMMENT '币种',
    `EXTRA_TEXT` VARCHAR(200)                   COMMENT '备注',
    `DATETIME` date                             COMMENT '消费时间',
    `STATUS` tinyint(4)  DEFAULT '1'            COMMENT '状态',
     PRIMARY KEY (`ID`),
     INDEX `CATEGORY` (`CATEGORY`),
     CONSTRAINT CATEGORY FOREIGN KEY(`CATEGORY`) REFERENCES ACC_CATEGORY(`ID`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='支出表';

CREATE TABLE IF NOT EXISTS `ACC_USER_ACCOUNT` (
    `ID` INT UNSIGNED AUTO_INCREMENT            COMMENT '用户记账表ID',
    `UID` INT UNSIGNED  NOT NULL                COMMENT '用户ID',
    `ACC_ID` INT UNSIGNED NOT NULL              COMMENT '消费表ID',
    PRIMARY KEY (`ID`),
    INDEX `UID` (`UID`),
    INDEX `ACC_ID` (`ACC_ID`),
    CONSTRAINT  USERID FOREIGN KEY(`UID`) REFERENCES ACC_USER(`ID`)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    CONSTRAINT  ACCID  FOREIGN KEY(`ACC_ID`) REFERENCES ACC_ACCOUNT(`ID`)
        ON DELETE CASCADE
        ON UPDATE CASCADE
)ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='用户记账表';

INSERT INTO ACC_CATEGORY(
ID,
CATEGORY
)VALUES('1','工资收入'),('2','饮食'),('3','服饰美容'),('4','生活日用'),('5','住房缴费'),('6','交通出行'),
('7','通讯物流'),('8','文教娱乐'),('9','运动健康'),('10','理财'),('11','保险'),('12','人情往来'),
('13','奖金收入'),('14','其他收入'),('15','其他支出');

INSERT INTO ACC_MONEY(
ID,
MONEY
)VALUES('1','RMB'),('2','USD');


