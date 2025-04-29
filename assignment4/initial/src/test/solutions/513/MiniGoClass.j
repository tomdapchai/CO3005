.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object
.field static final a I = 200
.field static y F

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label2:
	getstatic MiniGoClass/a I
	i2f
	getstatic MiniGoClass/y F
	fadd
	invokestatic io/putFloat(F)V
Label3:
Label1:
	return
.limit stack 2
.limit locals 1
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
	ldc 15.5
	iconst_2
	i2f
	fmul
	putstatic MiniGoClass/y F
Label1:
	return
.limit stack 3
.limit locals 0
.end method
