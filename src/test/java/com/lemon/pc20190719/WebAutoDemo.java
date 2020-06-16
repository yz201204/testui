package com.lemon.pc20190719;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

import org.apache.http.NameValuePair;
import org.apache.http.ParseException;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.testng.Assert;
import org.testng.annotations.AfterSuite;
import org.testng.annotations.BeforeSuite;
import org.testng.annotations.DataProvider;
import org.testng.annotations.Test;

import com.alibaba.fastjson.JSONPath;

import bsh.commands.dir;

public class WebAutoDemo {
	private WebDriver driver = null;
	
	@BeforeSuite
	public void init(){
		//�򿪻�������
		System.setProperty("webdriver.gecko.driver", "src/test/resources/geckodriver.exe");
		driver = new FirefoxDriver();
		
	}
	
	@Test(dataProvider="d1")
	public void test(String mobilephone,String password,String pwdconfirm) throws InterruptedException, ParseException, IOException{
		//����ע��ҳ��
		driver.get("http://test.lemonban.com/ningmengban/app/register/register.html");
		//�����ֻ���
		driver.findElement(By.id("username")).sendKeys(mobilephone);
		//��������
		driver.findElement(By.id("password")).sendKeys(password);
		//�����ظ�����
		driver.findElement(By.id("pwdconfirm")).sendKeys(pwdconfirm);
		//������֤��
		String verifycodeStoredInCookie = driver.manage().getCookieNamed("verifycode").getValue();
		driver.findElement(By.id("verifycode")).sendKeys(verifycodeStoredInCookie);
		//���ע��
		driver.findElement(By.id("signup-button")).click();
		Assert.assertTrue(false);
		Thread.sleep(1000);
	}
	
	@DataProvider(name="d1")
	public Object [][] datas(){
		Object [][] datas = {
								{"","",""},
								{"13517315120","",""},
								{"13517315120","123",""},
								{"13517315120","123456",""},
								{"13517315120","123456","123"},
								{"13517315120","123456","123456"}
						};
		return datas;
	}
	
	@AfterSuite
	public void tearDown(){
		driver.quit();
	}
	
	
}
