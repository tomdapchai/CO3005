.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object
.field static final a I = 200
.field static y F = 15.5

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label2:
	getstatic MiniGoClass/y F
	bipush 16
	i2f
	fcmpl
	iflt Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label4
Label8:
	getstatic MiniGoClass/a I
	invokestatic MiniGoClass/foo()I
	iadd
	invokestatic io/putInt(I)V
Label9:
	goto Label5
Label4:
Label10:
	getstatic MiniGoClass/a I
	invokestatic MiniGoClass/foo()I
	iadd
	iconst_1
	iadd
	invokestatic io/putInt(I)V
Label11:
Label5:
Label3:
Label1:
	return
.limit stack 6
.limit locals 1
.end method

.method public static foo()I
Label0:
Label2:
	iconst_1
	iconst_2
	iadd
	ireturn
Label3:
Label1:
.limit stack 4
.limit locals 0
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
