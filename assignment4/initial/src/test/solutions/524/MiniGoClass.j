.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object
.field static final a I = 5
.field static b I = 5

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label2:
.var 1 is x LPerson; from Label2 to Label3
	new Person
	dup
	invokespecial Person/<init>()V
	astore_1
	aload_1
	ldc "John"
	putfield Person/name Ljava/lang/String;
	aload_1
	bipush 30
	putfield Person/age I
.var 2 is y LPerson; from Label2 to Label3
	new Person
	dup
	invokespecial Person/<init>()V
	astore_2
	aload_2
	ldc "Doe"
	putfield Person/name Ljava/lang/String;
	aload_2
	bipush 25
	putfield Person/age I
	aload_1
	getfield Person/age I
	invokestatic io/putIntLn(I)V
	aload_1
	getfield Person/name Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
	aload_2
	getfield Person/age I
	invokestatic io/putIntLn(I)V
	aload_2
	getfield Person/name Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
	aload_1
	getfield Person/age I
	invokestatic io/putIntLn(I)V
	aload_1
	getfield Person/name Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label3:
Label1:
	return
.limit stack 3
.limit locals 3
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
