.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static isPalindrome(Ljava/lang/String;)Z
Label0:
.var 0 is str Ljava/lang/String; from Label0 to Label1
Label2:
.var 1 is len I from Label2 to Label3
	aload_0
	invokestatic MiniGoClass/length(Ljava/lang/String;)I
	istore_1
	iconst_0
.var 2 is i I from Label2 to Label3
	istore_2
Label6:
	iload_2
	iload_1
	iconst_2
	idiv
	if_icmpge Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifle Label5
Label9:
	aload_0
	iload_2
	invokestatic MiniGoClass/charAt(Ljava/lang/String;I)Ljava/lang/String;
	aload_0
	iload_1
	iload_2
	isub
	iconst_1
	isub
	invokestatic MiniGoClass/charAt(Ljava/lang/String;I)Ljava/lang/String;
	invokevirtual java/lang/String/compareTo(Ljava/lang/String;)I
	ifeq Label13
	iconst_1
	goto Label14
Label13:
	iconst_0
Label14:
	ifle Label11
Label15:
	iconst_0
	ireturn
Label16:
Label11:
Label10:
Label4:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label6
Label5:
	iconst_1
	ireturn
Label3:
Label1:
.limit stack 11
.limit locals 3
.end method

.method public static length(Ljava/lang/String;)I
Label0:
.var 0 is str Ljava/lang/String; from Label0 to Label1
Label2:
	iconst_5
	ireturn
Label3:
Label1:
.limit stack 2
.limit locals 1
.end method

.method public static charAt(Ljava/lang/String;I)Ljava/lang/String;
Label0:
.var 0 is str Ljava/lang/String; from Label0 to Label1
.var 1 is idx I from Label0 to Label1
Label2:
	aload_0
	ldc "radar"
	invokevirtual java/lang/String/compareTo(Ljava/lang/String;)I
	ifne Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label4
Label8:
.var 2 is chars [Ljava/lang/String; from Label8 to Label9
	iconst_5
	anewarray java/lang/String
	dup
	iconst_0
	ldc "r"
	aastore
	dup
	iconst_1
	ldc "a"
	aastore
	dup
	iconst_2
	ldc "d"
	aastore
	dup
	iconst_3
	ldc "a"
	aastore
	dup
	iconst_4
	ldc "r"
	aastore
	astore_2
	aload_2
	iload_1
	aaload
	areturn
Label9:
	goto Label5
Label4:
Label10:
.var 2 is chars [Ljava/lang/String; from Label10 to Label11
	iconst_5
	anewarray java/lang/String
	dup
	iconst_0
	ldc "h"
	aastore
	dup
	iconst_1
	ldc "e"
	aastore
	dup
	iconst_2
	ldc "l"
	aastore
	dup
	iconst_3
	ldc "l"
	aastore
	dup
	iconst_4
	ldc "o"
	aastore
	astore_2
	aload_2
	iload_1
	aaload
	areturn
Label11:
Label5:
	ldc ""
	areturn
Label3:
Label1:
.limit stack 9
.limit locals 3
.end method

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label2:
	ldc "Is 'radar' a palindrome?"
	invokestatic io/putStringLn(Ljava/lang/String;)V
	ldc "radar"
	invokestatic MiniGoClass/isPalindrome(Ljava/lang/String;)Z
	invokestatic io/putBoolLn(Z)V
	ldc "Is 'hello' a palindrome?"
	invokestatic io/putStringLn(Ljava/lang/String;)V
	ldc "hello"
	invokestatic MiniGoClass/isPalindrome(Ljava/lang/String;)Z
	invokestatic io/putBoolLn(Z)V
Label3:
Label1:
	return
.limit stack 1
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
Label1:
	return
.limit stack 0
.limit locals 0
.end method
