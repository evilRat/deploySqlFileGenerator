CREATE TABLE `znyd_h5onelgn_info` (
    `msisdn` varchar(20) NOT NULL COMMENT '加密后的手机号',
    `passid` varchar(64) NOT NULL COMMENT '用户统一账号的系统标识',
    `msisdnmask` varchar(20) NOT NULL COMMENT '手机号码掩码',
    `createTime` datetime DEFAULT NULL COMMENT '创建时间',
    `field1` varchar(60) DEFAULT NULL COMMENT '最近修改人',
    `field2` varchar(0) DEFAULT NULL COMMENT '最近修改时间',
    `billId` varchar(255) NOT NULL COMMENT '手机号码',
    PRIMARY KEY (`billId`)
);
CREATE TABLE `znyd_h5login_info` (
    `rowId` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键id',
    `businessKey` varchar(64) DEFAULT NULL COMMENT '业务主键',
    `billId` varchar(60) DEFAULT NULL COMMENT '手机号',
    `loginTime` datetime DEFAULT NULL COMMENT '登录时间',
    `loginMode` char(2) NOT NULL COMMENT '登录方式:0短信登录,1一键登录',
    `accessChannels` varchar(60) NOT NULL COMMENT '登录渠道 用来区分短信、互联网等渠道',
    `field1` varchar(60) DEFAULT NULL COMMENT '备用字段1',
    `field2` varchar(255) DEFAULT NULL COMMENT '备用字段',
    PRIMARY KEY (`rowId`)
);
insert into
    nk_camel_keys
values
    (1, 'USER_ID', 'userId', '');
insert into
    nk_camel_keys
values
    (2, 'RETINFO', 'retinfo', '');
insert into
    nk_camel_keys
values
    (3, 'OFFER_LIST', 'offerList', '');
insert into
    nk_camel_keys
values
    (4, 'OFFER_INFO', 'offerInfo', '');
insert into
    nk_camel_keys
values
    (5, 'OFFER_ID', 'offerId', '');
insert into
    nk_camel_keys
values
    (6, 'OFFER_NAME', 'offerName', '');
insert into
    nk_camel_keys
values
    (7, 'UP_OFFER_ID', 'upOfferId', '');
insert into
    nk_camel_keys
values
    (8, 'UP_OFFER_NAME', 'upOfferName', '');
insert into
    nk_camel_keys
values
    (9, 'IS_PACKAGE', 'isPackage', '');
insert into
    nk_camel_keys
values
    (10, 'SP_CODE', 'spCode', '');
insert into
    nk_camel_keys
values
    (11, 'BIZ_CODE', 'bizCode', '');
insert into
    nk_camel_keys
values
    (12, 'SP_NAME', 'spName', '');
insert into
    nk_camel_keys
values
    (13, 'BILL_TYPE', 'billType', '');
insert into
    nk_camel_keys
values
    (14, 'OFFER_PRICE', 'offerPrice', '');
insert into
    nk_camel_keys
values
    (15, 'STATUS', 'status', '');
insert into
    nk_camel_keys
values
    (16, 'ORDER_TIME', 'orderTime', '');
insert into
    nk_camel_keys
values
    (17, 'OFFER_DESC', 'offerDesc', '');
insert into
    nk_camel_keys
values
    (18, 'OFFER_TYPE', 'offerType', '');
insert into
    nk_camel_keys
values
    (19, 'OFFER_TYPE_NAME', 'offerTypeName', '');
insert into
    nk_camel_keys
values
    (20, 'BRAND_ID', 'brandId', '');
insert into
    nk_camel_keys
values
    (21, 'BRAND_NAME', 'brandName', '');
insert into
    nk_camel_keys
values
    (22, 'IS_MAIN', 'isMain', '');
insert into
    nk_camel_keys
values
    (23, 'CHOOSE_TAG', 'chooseTag', '');
insert into
    nk_camel_keys
values
    (24, 'CAN_UN_SUB', 'canUnSub', '');
insert into
    nk_camel_keys
values
    (25, 'EFF_TIME', 'effTime', '');
insert into
    nk_camel_keys
values
    (26, 'EXP_TIME', 'exp_time', '');
insert into
    nk_camel_keys
values
    (27, 'OFFER_ATTR_LIST', 'offerAttrList', '');
insert into
    nk_camel_keys
values
    (28, 'OFFER_ATTR', 'offerAttr', '');
insert into
    nk_camel_keys
values
    (29, 'ATTR_ID', 'attrId', '');
insert into
    nk_camel_keys
values
    (30, 'ATTR_NAME', 'attrName', '');
insert into
    nk_camel_keys
values
    (31, 'ATTR_DESC', 'attrDesc', '');
insert into
    nk_camel_keys
values
    (32, 'ATTR_VALUE', 'attrValue', '');
insert into
    nk_camel_keys
values
    (33, 'ATTR_VALUE_DESC', 'attrValueDesc', '');
insert into
    nk_camel_keys
values
    (34, 'ORDER_STAFF_ID', 'orderStaffId', '');
insert into
    nk_camel_keys
values
    (35, 'ORDER_CHNN', 'orderChnn', '');
insert into
    nk_camel_keys
values
    (36, 'REMARK', 'remark', '');
insert into
    nk_camel_keys
values
    (37, 'STARTORDERTIME', 'startordertime', '');
insert into
    nk_camel_keys
values
    (38, 'CLOSEORDERTIME', 'closeordertime', '');
insert into
    nk_camel_keys
values
    (39, 'BIZNAME', 'bizname', '');
insert into
    nk_camel_keys
values
    (40, 'SPTYPE', 'sptype', '');
insert into
    nk_camel_keys
values
    (41, 'ORDER_DEP', 'orderDep', '');
insert into
    nk_camel_keys
values
    (42, 'SHORT_NUM', 'shortNum', '');
insert into
    nk_camel_keys
values
    (43, 'ERRORINFO', 'errorinfo', '');
insert into
    nk_camel_keys
values
    (44, 'CODE', 'code', '');
insert into
    nk_camel_keys
values
    (45, 'MESSAGE', 'message', '');
insert into
    nk_camel_keys
values
    (46, 'BUSI_SERIAL_NO', 'busiSerialNo', '');
update
    city_code_data
set
    city_code = concat('0', city_code)
where
    id > 0;