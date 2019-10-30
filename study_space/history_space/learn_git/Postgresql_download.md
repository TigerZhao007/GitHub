
# PostgreSQL安装详细步骤（windows）




# 配置用户及权限

CREATE TABLE public."User"
(
    id bigint,
    name text COLLATE pg_catalog."default",
    password text COLLATE pg_catalog."default",
    level bigint,
    token text COLLATE pg_catalog."default",
    type text COLLATE pg_catalog."default"
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public."User"
    OWNER to postgres;
	
ALTER TABLE public."peochr"
    OWNER to ga;	
	
添加表
1-yik-password-0-无-管理员



