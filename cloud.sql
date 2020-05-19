/*
 Navicat Premium Data Transfer

 Source Server         : root
 Source Server Type    : MySQL
 Source Server Version : 80013
 Source Host           : localhost:3306
 Source Schema         : cloud

 Target Server Type    : MySQL
 Target Server Version : 80013
 File Encoding         : 65001

 Date: 25/06/2019 09:29:35
*/

SET NAMES utf8;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for case1
-- ----------------------------
DROP TABLE IF EXISTS `case1`;
CREATE TABLE `case1`  (
  `caseid` int(11) NOT NULL,
  `casename` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `ip` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `port` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `createtime` datetime(0) NULL DEFAULT NULL,
  PRIMARY KEY (`caseid`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of case1
-- ----------------------------
INSERT INTO `case1` VALUES (1, 'aaa', '127.0.0.1', '2003', '2019-06-23 19:48:45');
INSERT INTO `case1` VALUES (2, 'bbb', '202.117.10.37', '2003', '2019-06-23 19:49:13');

-- ----------------------------
-- Table structure for node
-- ----------------------------
DROP TABLE IF EXISTS `node`;
CREATE TABLE `node`  (
  `nodeid` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `nodename` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `platform` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `systembit` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `state` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `createtime` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of node
-- ----------------------------
INSERT INTO `node` VALUES ('001', 'haha', 'Linux', '64', 'running', '2019-06-23');
INSERT INTO `node` VALUES ('002', 'haha', 'Linux', '64', 'running', '2019-06-23 19:43:32');
INSERT INTO `node` VALUES ('003', 'haha', 'Linux', '64', 'running', '2019-06-23 19:43:56');
INSERT INTO `node` VALUES ('123', '1@2.com', '1234', '006', 'running', '2019-06-24');

-- ----------------------------
-- Table structure for user1
-- ----------------------------
DROP TABLE IF EXISTS `user1`;
CREATE TABLE `user1`  (
  `iden` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `username` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `role` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `imageid` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `password` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `idenpassword` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `createtime` datetime(0) NULL DEFAULT NULL,
  `index1` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of user1
-- ----------------------------
INSERT INTO `user1` VALUES ('610425199509200261', '1@1.com', '≥¨º∂”√ªß', '003', '1', '1', '2019-06-24 16:37:23', '1');
INSERT INTO `user1` VALUES ('1234', '1@3.com', '12345', '3', '3', '3', '2019-06-24 23:25:21', '0');
INSERT INTO `user1` VALUES ('123', '1@2.com', '1234', '006', '2', '2', '2019-06-24 23:36:16', '1');
INSERT INTO `user1` VALUES ('666', '1@2.com', '1234', '1@2.com', '2', '2', '2019-06-24 23:58:34', '1');

SET FOREIGN_KEY_CHECKS = 1;
