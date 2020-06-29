#Q1
K<-100

fct<-function(x){
  if(x-K>0){
    x-K
  }
  else{
    0
  }
}

fct = Vectorize(fct)
curve(fct,
      from= 0, to=200,
      col = "dark blue",
      xname = "주식 St",)


#Q2
bsm<-function(s,k,t,sd,r){
  d1 <- (log(s/k) + t*(r + 0.5*sd^2)) / (sd * sqrt(t))
  d2 <- d1 - sd*sqrt(t)
  c <- s*pnorm(d1, mean = 0, sd = 1) - (k*(exp(1)^((-r)*t))*pnorm(d2, mean = 0, sd = 1))
  return (c)
}

print(bsm(100,100,0.5,0.1,0.04))

#Q3
making_curst<-function(s,t,r,tl,sd){
  cur_st <- s
  loop_time <- t/tl
  for(i in 1:loop_time){
    cur_st = cur_st*exp((r-0.5*(sd^2))*tl + sd*sqrt(tl)*rnorm(1))
  }
  return (cur_st)
}

draw_graph<-function(t,loop_time,data){
  plot(seq(0,t,length = loop_time),data,main = "First 5 Path", xlab = "T", ylab = "path", type = 'l', col = "dark blue")
}

newbsm<-function(s,k,t,sd,r,tl,N){
  temp_for_graph <- c()
  new_s <- s
  sigma_v <- 0
  loop_time<-t/tl
  for(j in 1:N){
    if(j<=5){
      for(i in 1:loop_time){
        new_s = new_s*exp((r-0.5*(sd^2))*tl + sd*sqrt(tl)*rnorm(1))
        temp_for_graph = c(temp_for_graph,new_s)
      }
      draw_graph(t,loop_time,temp_for_graph)
      temp_for_graph = c()
    }
    sigma_v <- sigma_v + max(making_curst(s,t,r,tl,sd) - k, 0)
  }
  c<-exp(-r*t)/10000*sigma_v
  print(c)
}

newbsm(100,100,0.5,0.1,0.04,0.001,10000)

