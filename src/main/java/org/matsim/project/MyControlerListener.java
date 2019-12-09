package org.matsim.project;
import	org.apache.log4j.Logger;
import	org.matsim.core.controler.events.*;
import	org.matsim.core.controler.listener.*;
public	class	MyControlerListener	implements StartupListener, ShutdownListener, IterationStartsListener, ScoringListener {
    private	final	static	Logger	log	=	Logger.getLogger(MyControlerListener.class);

    @Override
    public	void	notifyIterationStarts(IterationStartsEvent	iterationStartsEvent)	{
        log.info("What	will	happen	in	iteration	"	+	iterationStartsEvent.getIteration()	+	"?");
    }
    @Override
    public	void	notifyScoring(ScoringEvent	scoringEvent)	{
        log.info("Let's	evaluate!");
    }
    @Override
    public	void	notifyStartup(StartupEvent	startupEvent)	{
        log.info("We're	starting!");
    }
    @Override
    public	void	notifyShutdown(ShutdownEvent	shutdownEvent)	{
        log.info("Bye,	it's	over!");
    }
}
