
/**
* public 表示公开的
* class 表示定义一个类
* HelloWorld 表示一个类名
*/
public class HelloWorld{ //表示定义一个公开的类，类名为HelloWorld
	
    // 类体
	/*
	public 表示公开的
	static 表示静态的
	void 表示为空
	main 表示方法名是main
	（string[] args)是一个main方法的形式参数列表
	
	需要记住的是：
	以下的方法是一个程序的主方法，是程序的执行入口
	是sun公司规定的，固定的方法
	*/
	public static void main(String[] args){ // 表示定义一个公开的静态的主方法
		// 方法体；
		// 方法体
		/*
		java语句以分号终止，分号必须是半角分号
		先记住：以下这样代码的作用是向控制台输出一段消息
		以下的双引号必须是半角的双引号，是java语法的一部分
		java中所有的字符串都使用双引号括起来
		*/
		System.out.println("Hello world!");
		
		// 再次向控制台输出消息
		System.out.println("hello java!");
		
		// 输出中文
		System.out.println("您好，杰克！");
		
		// 输出中文
		System.out.println("您好，杰“克”！"); //这里双引号为全角，换成半角就错了		
	}
}


//单行注释

/*
多行注释
*/

/** 比较专业的注释方式
*
*
*
*/
