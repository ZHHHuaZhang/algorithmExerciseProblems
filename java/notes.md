# IntelliJ idea 
免费三十天
## 追加依赖
https://blog.csdn.net/m0_50207524/article/details/136427033

# maven 
需要配置国内镜像源
# spring boot
##  项目启动
[前端开发 Spring Boot 入门指南：demo-crud 实现增删改查](https://juejin.cn/post/7389057936738369546?searchId=20241111105859148ABF7E75A472939017)
## 注解
@RestController 是 Spring 框架中的一个注解，用于标记一个类为 RESTful 控制器。这个注解结合了 @Controller 和 @ResponseBody 的功能

@Controller 注解用于标记一个类作为 Spring MVC 控制器。它告诉 Spring 这个类将处理来自用户的请求。控制器类通常包含多个方法，每个方法都映射到一个或多个 URL 请求

白话：其实就是用来定义接口的

@ResponseBody 注解用于方法级别，表示该方法的返回值应该直接写入 HTTP 响应体中，而不是作为视图模型的一部分来渲染视图。这意味着如果方法返回的是 Java 对象，Spring 将尝试将其序列化为相应的格式（如 JSON 或 XML）并发送给客户端
白话：这里处理的就是前端接口返回的数据信息，表示方法的返回值应该直接写入 HTTP 响应体
总结：定义了接口，并且包装了返回给前端的数据格式 这里指 HTTP响应体，不是说的业务封装的 code 等

@RequestMapping 是 Spring MVC 框架中的一个核心注解，用于建立 Web 请求与处理器方法之间的映射关系。它可以作用于类级别或方法级别，用于指定哪些 HTTP 请求（URL 和请求类型）应该映射到特定的控制器类或其方法上

定义接口，还可以增加接口前缀，被 GetMapping 等进行了二次包装
 ### Lombok
 用来生成实体类 Getter 和 Setter 架包
 不使用 Lombok 的情况
 ![alt text](/java/img/image.png)
使用的情况
![](img/![](img/2024-11-11-22-27-27.png).png)