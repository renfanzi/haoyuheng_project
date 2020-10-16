设计文档



### 一、编写目的

本文档的编制是为了让客户和软件开发者双方对该开发软件的初始规定有一个共同的理解，定义所要开发目标，包括对功能的规定和性能的要求，指出预期的系统用户、系统的运行环境以及对用户操作的约定，使之成为整个项目中软件产品开发设计与实现的根据，也是软件产品的测试和验收的依据。该说明书的读者为该项目的客户以及项目开发人员。



### 二、背景

1. 本系统名称：航天装备技术开源网络知识库

2. 客户对接人员：

   本系统开发单位：

   本系统的用户：

3.本系统的开发工具采用：

​		a. PYTHON: 3.7.0

​		b. MYSQL: 5.7 

4.该系统同其他系统(或机构)的基本相互往来关系：该系统基于chrome浏览器，版本为 85.0.4183.83（正式版本)（64 位），支持Windows系列平台 

5.本系统为Windows平台下B/S模式网络版。

### 三、开发任务计划

| 任务           | 时间  | 进度   | 要求                                                         |
| -------------- | ----- | ------ | ------------------------------------------------------------ |
| 1. 数据库设计  | 0.5天 | 完成   | 无                                                           |
| 2. 产品设计    | 0.5天 | 完成   | 无                                                           |
| 3. 爬取数据    | 10天  | 进行中 | 爬取需要数据                                                 |
| 4. 数据清洗    |       |        | 爬取数据的时候，就需要剔除无用数据，并进行规范化，增加工作量 |
| 5. web模块开发 | 1天   | 未开发 | 数据请求接口                                                 |

### 四、数据库表设计

1. ##### 论文详情表

   表名

   ```
   xueshu_paper
   ```

   字段设计

   | 字段                       | 类型             | 说明                                                   |
   | -------------------------- | ---------------- | ------------------------------------------------------ |
   | id                         | int              | id                                                     |
   | technology_crawler_keyword | varchar(200)     | 技术体系（爬虫搜索关键字）                             |
   | article_paperid            | varchar(200)     | 百度学术的id：paperid=e0e89fe616264a497a8fd6009decfcb6 |
   | article_title              | varchar(200)     | 标题                                                   |
   | article_abstract           | text             | 摘要                                                   |
   | article_keyword            | text(json)       | 关键字(json后的数组形式)                               |
   | article_doi                | text             | DOI                                                    |
   | article_sc_cited           | varchar(50)      | 被引用量                                               |
   | article_year               | varchar(50)      | 年份                                                   |
   | article_journal_title      | varchar(50)      | 来源期刊                                               |
   | article_dl_list            | text(json(数组)) | 全部来源（例如万方，知网等）                           |
   | article_sc_search          | text(json(数组)) | 研究点分析（['计算流体力学', '空气动力学'...]）        |
   | article_createtime         | int              | 数据写入时间（GTM格式）                                |
   | article_createdatetime     | varchar(200)     | 数据写入时间（字符串时间）                             |

   SQL创建表字段

   ```sql
   CREATE TABLE `xueshu_paper` (
     `id` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '主键ID',
     `technology_crawler_keyword` varchar(200) NOT NULL DEFAULT '' COMMENT '技术体系（爬虫搜索关键字）',
     `article_paperid` varchar(200) NOT NULL DEFAULT '' COMMENT '百度学术的id',
     `article_title` varchar(200) NOT NULL DEFAULT '' COMMENT '标题',
     `article_abstract` text NOT NULL DEFAULT '' COMMENT '摘要',
     `article_keyword` text NOT NULL DEFAULT '' COMMENT '关键字',
     `article_doi` varchar(200) NOT NULL DEFAULT '' COMMENT 'DOI',
     `article_sc_cited` varchar(200) NOT NULL DEFAULT '' COMMENT '被引用量',
     `article_year` varchar(200) NOT NULL DEFAULT '' COMMENT '年份',
     `article_journal_title` varchar(200) NOT NULL DEFAULT '' COMMENT '来源期刊',
     `article_dl_list` text NOT NULL DEFAULT '' COMMENT '全部来源',
     `article_sc_search` text NOT NULL DEFAULT '' COMMENT '研究点分析',
     `article_createtime` int(11) NOT NULL DEFAULT '' COMMENT '数据写入时间（GTM格式）',
     `article_createdatetime` varchar(200) NOT NULL DEFAULT '' COMMENT '数据写入时间（字符串时间）',
     PRIMARY KEY (`id`) USING BTREE
   ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT COMMENT='论文详情表';
   ```

   

2. ##### 论文作者表

   表名

   ```
   xueshu_authors
   ```

   字段设计

   | 字段                  | 类型         | 说明                       |
   | --------------------- | ------------ | -------------------------- |
   | id                    | int          | id                         |
   | xueshu_paper_id       | int          | 关联论文表id               |
   | author_name           | varchar      | 作者姓名                   |
   | author_organization   | varchar      | 作者组织机构               |
   | author_url            | varchar      | 作者相关链接               |
   | author_createtime     | int          | 数据写入时间（GTM格式）    |
   | author_createdatetime | varchar(200) | 数据写入时间（字符串时间） |

   SQL创建表字段

   ```sql
   CREATE TABLE `xueshu_authors` (
     `id` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '主键ID',
     `xueshu_paper_id` int(11) NOT NULL DEFAULT '' COMMENT '关联论文表id',
     `author_name` varchar(200) NOT NULL DEFAULT '' COMMENT '作者姓名',
     `author_organization` varchar(200) NOT NULL DEFAULT '' COMMENT '作者组织机构',
     `author_url` varchar(200) NOT NULL DEFAULT '' COMMENT '作者相关链接',
     `author_createtime` int(11) NOT NULL DEFAULT '' COMMENT '数据写入时间（GTM格式）',
     `author_createdatetime` varchar(200) NOT NULL DEFAULT '' COMMENT '数据写入时间（字符串时间）',
     PRIMARY KEY (`id`) USING BTREE
   ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT COMMENT='论文作者表';
   ```

   

3. ##### 论文相似文献 和 论文参考文献

   表名

   ```
   xueshu_similar_references
   ```

   字段设计

   | 字段              | 类型                 | 说明                       |
   | ----------------- | -------------------- | -------------------------- |
   | id                | int                  | id                         |
   | xueshu_paper_id   | int                  | 关联论文表id               |
   | sc_type           | int                  | 1：相似文献，2：参考文献   |
   | sc_pdf_read       | varchar              | pdf链接                    |
   | sc_research       | text(json([ ]))      | 研究点分析                 |
   | sc_abstract       | text                 | 摘要                       |
   | sc_keyword        | varchar（json）      | 关键字                     |
   | sc_year           | varchar              | 年份                       |
   | sc_title          | varchar              | 标题                       |
   | url               | varchar              | url链接                    |
   | sc_scholarurl     | varchar              | 学者链接                   |
   | sc_author         | text（json（【】）） | 学者信息                   |
   | sc_createtime     | int                  | 数据写入时间（GTM格式）    |
   | sc_createdatetime | varchar(200)         | 数据写入时间（字符串时间） |

   SQL创建表字段

   ```sql
   CREATE TABLE `xueshu_similar_references` (
     `id` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '主键ID',
     `xueshu_paper_id` int(11) NOT NULL DEFAULT '' COMMENT '关联论文表id',
     `sc_type` int(11) NOT NULL DEFAULT '' COMMENT '1：相似文献，2：参考文献',
     `sc_pdf_read` varchar(200) NOT NULL DEFAULT '' COMMENT 'pdf链接',
     `sc_research` varchar(200) NOT NULL DEFAULT '' COMMENT '研究点分析',
     `sc_abstract` varchar(200) NOT NULL DEFAULT '' COMMENT '摘要',
     `sc_keyword` varchar(200) NOT NULL DEFAULT '' COMMENT '关键字',
     `sc_year` varchar(200) NOT NULL DEFAULT '' COMMENT '年份',
     `sc_title` varchar(200) NOT NULL DEFAULT '' COMMENT '标题',
     `url` varchar(200) NOT NULL DEFAULT '' COMMENT 'url链接',
     `sc_scholarurl` text NOT NULL DEFAULT '' COMMENT '学者链接',
     `sc_author` text NOT NULL DEFAULT '' COMMENT '作者信息',
     `sc_createtime` int(11) NOT NULL DEFAULT '' COMMENT '数据写入时间（GTM格式）',
     `sc_createdatetime` varchar(200) NOT NULL DEFAULT '' COMMENT '数据写入时间（字符串时间）',
     PRIMARY KEY (`id`) USING BTREE
   ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT COMMENT='论文相似文献 和 论文参考文献';
   ```

   



