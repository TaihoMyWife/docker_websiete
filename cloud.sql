/*
Navicat MySQL Data Transfer

Source Server         : localhost_3306
Source Server Version : 50709
Source Host           : localhost:3306
Source Database       : cloud

Target Server Type    : MYSQL
Target Server Version : 50709
File Encoding         : 65001

Date: 2019-07-26 10:57:08
*/

SET FOREIGN_KEY_CHECKS=0;
-- ----------------------------
-- Table structure for `case1`
-- ----------------------------
DROP TABLE IF EXISTS `case1`;
CREATE TABLE `case1` (
  `caseid` int(11) NOT NULL,
  `casename` varchar(255) DEFAULT NULL,
  `ip` varchar(255) DEFAULT NULL,
  `port` varchar(255) DEFAULT NULL,
  `createtime` datetime DEFAULT NULL,
  PRIMARY KEY (`caseid`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of case1
-- ----------------------------
INSERT INTO `case1` VALUES ('1', 'aaa', '127.0.0.1', '2003', '2019-06-23 19:48:45');

-- ----------------------------
-- Table structure for `node`
-- ----------------------------
DROP TABLE IF EXISTS `node`;
CREATE TABLE `node` (
  `nodeid` varchar(255) DEFAULT NULL,
  `nodename` varchar(255) DEFAULT NULL,
  `platform` varchar(255) DEFAULT NULL,
  `systembit` varchar(255) DEFAULT NULL,
  `state` varchar(255) DEFAULT NULL,
  `createtime` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of node
-- ----------------------------
INSERT INTO `node` VALUES ('001', 'haha', 'Linux', '64位', 'running', '2019-06-23');
INSERT INTO `node` VALUES ('002', 'haha', 'Linux', '64位', 'running', '2019-06-23 19:43:32');
INSERT INTO `node` VALUES ('003', 'haha', 'Linux', '64位', 'running', '2019-06-23 19:43:56');

-- ----------------------------
-- Table structure for `user1`
-- ----------------------------
DROP TABLE IF EXISTS `user1`;
CREATE TABLE `user1` (
  `iden` varchar(255) DEFAULT NULL,
  `username` varchar(255) DEFAULT NULL,
  `role` varchar(255) DEFAULT NULL,
  `imageid` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `idenpassword` varchar(255) DEFAULT NULL,
  `createtime` datetime DEFAULT NULL,
  `index1` varchar(255) DEFAULT NULL,
  `authority` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of user1
-- ----------------------------
INSERT INTO `user1` VALUES ('610425199509200261', '1@1.com', '普通用户', '003', '1234', '1', '2019-06-24 16:37:23', '2', '1');
INSERT INTO `user1` VALUES ('1234', '1@3.com', '12345', '3', '1234', '3', '2019-06-24 23:25:21', '1', '0');
INSERT INTO `user1` VALUES ('123', '1@2.com', '1234', '006', '1234', '2', '2019-06-24 23:36:16', '1', '0');
INSERT INTO `user1` VALUES ('666', '1@2.com', '1234', '1@2.com', '1234', '2', '2019-06-24 23:58:34', '2', '0');
INSERT INTO `user1` VALUES ('123', '15127@qq.com', '123', '002', '1234', '123', '2019-06-29 16:26:32', '0', '0');
INSERT INTO `user1` VALUES ('1234567890', '15127@qq.com', 'regular', '002', '1234', '123456', '2019-06-30 07:59:52', '0', '0');
