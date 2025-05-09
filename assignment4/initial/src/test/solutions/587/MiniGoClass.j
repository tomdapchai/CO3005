.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label2:
.var 1 is str1 Ljava/lang/String; from Label2 to Label3
	ldc "Hello"
	astore_1
.var 2 is str2 Ljava/lang/String; from Label2 to Label3
	ldc "World"
	astore_2
.var 3 is str3 Ljava/lang/String; from Label2 to Label3
	aload_1
	ldc " "
	invokevirtual java/lang/String/concat(Ljava/lang/String;)Ljava/lang/String;
	aload_2
	invokevirtual java/lang/String/concat(Ljava/lang/String;)Ljava/lang/String;
	astore_3
	aload_3
	invokestatic io/putStringLn(Ljava/lang/String;)V
	aload_1
	aload_2
	invokevirtual java/lang/String/compareTo(Ljava/lang/String;)I
	ifle Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	invokestatic io/putBoolLn(Z)V
	ldc "abc"
	ldc "abc"
	invokevirtual java/lang/String/compareTo(Ljava/lang/String;)I
	ifne Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	invokestatic io/putBoolLn(Z)V
Label3:
Label1:
	return
.limit stack 7
.limit locals 4
.end method

.method public <init>()V
.var 0 is this LMiniGoClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static <clinit>()V
Label0:
Label1:
	return
.limit stack 0
.limit locals 0
.end method
